from __future__ import annotations
from re import L
from typing import Callable, List, Set, Union, Optional, Any
from pydash.objects import get, set_ # type: ignore
from pydantic import BaseModel, Field
from time import time_ns
from hashlib import sha256
from uuid import uuid4

from graph_parse.enums import ComparitiveOperationEnum, TraversalEventEnum, NodeModeEnum
from graph_parse.helpers import iterables_intersect, nested_getattr, camel_to_snake, format_alias, path_list_to_str


class Node:
    __path: List[str]
    
    def __init__(self, path=[], value=None, **kwargs):
        self.__path = path or [self.class_snake_name]
        self.__value = value or self

        globals()[f"node_{self.class_snake_name}"] = self.__class__

        for name in self.__annotations__:
            if name.startswith("_Node__"):
                continue

            new_path = self.__path + [name]
            new_value = kwargs.get(format_alias(name))
            new_kwargs = new_value.to_dict() if isinstance(new_value, Node) else {}

            private_name = f"_{name}"

            setattr(self, private_name, Node(path=new_path, value=new_value, **new_kwargs))
            setattr(self.__class__, name, property(self.create_getter(private_name)))

    def __call__(self) -> Path:
        return Path(self.__path)

    def to_dict(self) -> dict:
        result = {}

        for name in self.__annotations__:
            if name.startswith("_Node__"):
                continue 

            value = getattr(self, name)
            if isinstance(value, Node):
                value = value.to_dict() 

            key = format_alias(name)
            result[key] = value or None 

        return result

    def create_getter(self, private_prop_name: str) -> Callable:
        def getter(self):
            return nested_getattr(self, [private_prop_name, "_Node__value"])
        return getter

    def to_pydantic(self) -> BaseModel:
        return type(f"Pydantic{self.__class__.__name__}", (BaseModel,), {
            "__annotations__": self.__annotations__
        })(**self.to_dict())

    def from_pydantic(self, pydantic_model: BaseModel, mode: NodeModeEnum = NodeModeEnum.Data) -> Node:
        return type(pydantic_model.__class__.__name__, (Node,), {
            "__annotations__": pydantic_model.__annotations__
        })(**(pydantic_model.dict() if mode == NodeModeEnum.Data else {}))

    @property
    def class_snake_name(self) -> str:
        return camel_to_snake(self.__class__.__name__)

class Path:
    value: List[str]

    def __init__(self, value: List[str]):
        self.value = value

    def __str__(self):
        return path_list_to_str(self.value)

    def __hash__(self):
        return hash(tuple(self.value))

    def __add__(self, other_path: Path):
        return Path(self.value + other_path.value)
    
    def __eq__(self, other: object):
        if not isinstance(other, Path):
            return NotImplemented
        return tuple(self.value) == tuple(other.value)

class Edge:
    source: Path
    sink: Path
    function: Optional[Callable]

    def __init__(self, source: Path, sink: Path, function: Callable = None):
        self.source = source
        self.sink = sink
        self.function = function

    def __str__(self):
        return f"{str(self.source)}->{f'{self.function.__name__}({str(self.sink)})' if self.function else str(self.sink)}"

    def __hash__(self):
        return hash(str(self))


class GraphState:
    value: dict 

    def __init__(self, value: dict = {}) -> None:
        self.value = value 

    def __setitem__(self, key: Path, value: Any):
        self.value = set_(self.value, key.value, value)

    def __getitem__(self, key: Path):
        return get(self.value, key.value)

    def flatten(self, path: Optional[Path] = None):
        result = {}
        for k, v in self.value.items():
            new_sub_path = Path([k])
            new_path = (path + new_sub_path) if path else new_sub_path
            
            if isinstance(v, dict):
                sub_state = GraphState(value=v)
                result.update(sub_state.flatten(path=new_path))
            
            result[new_path] = v
        return result.items()

class Event(BaseModel):
    type: TraversalEventEnum
    time: int = Field(default_factory=time_ns)
    graph_hash: int
    traversal_id: str
    
    payload: Optional[dict]

class Graph:
    edges: List[Edge] 
    outputs: List[str]
    event_handler: Optional[Callable]

    def __init__(self, edges: List[Edge] = [], outputs: List[str] = [], event_handler: Optional[Callable] = None):
        self.edges = edges
        self.outputs = outputs
        self.event_handler = event_handler

    def __str__(self):
        return '&'.join(sorted(str(edge) for edge in self.edges))

    def __hash__(self):
        return int.from_bytes(sha256(str(self).encode()).digest())

    def traverse(self, *args: Union[Node, BaseModel], outputs: List[str] = []) -> dict:
        if outputs:
            subgraph = self.create_subgraph(outputs)
            return subgraph.traverse(*args)

        self.traversal_id = str(uuid4())

        node_args = [arg if isinstance(arg, Node) else Node().from_pydantic(arg) for arg in args]
        state = GraphState(value={node_arg.class_snake_name: node_arg.to_dict() for node_arg in node_args})

        edges_traversed: Set[Edge] = set()
        complete = False

        self.trigger_event(TraversalEventEnum.TraversalStarted)

        while not complete:
            complete = True
            flattened_state = state.flatten()

            for path, value in flattened_state:
                edges = self.search(source=path, exclude=edges_traversed)
                if not edges:
                    continue
                
                complete = False

                for edge in edges:
                    self.trigger_event(TraversalEventEnum.EdgeStarted, edge=str(edge))
                    
                    value = state[edge.source]
                    
                    if edge.function:
                        if self.search(sink=edge.source, comparitive_operator=ComparitiveOperationEnum.Intersect, exclude=edges_traversed.union({edge})):
                            continue
                        
                        input_model = edge.function.__annotations__[edge.source.value[-1]]
                        input = input_model(**value) if issubclass(input_model, Node) else value
                        try:
                            output = edge.function(input)
                        except Exception as e:
                            if self.trigger_event(TraversalEventEnum.EdgeException, edge=str(edge), exception=str(e)):
                                output = None
                            else:
                                raise e
                        value = output.to_dict() if isinstance(output, Node) else output

                    state[edge.sink] = value
                    edges_traversed.add(edge)

                    self.trigger_event(TraversalEventEnum.EdgeEnded)

        self.trigger_event(TraversalEventEnum.TraversalEnded, state=state.value)

        result = {}
        for name in self.outputs or state.value:
            data = state.value.get(name)
            value = model(**data) if (model := globals().get(f"node_{name}")) and data else data
            result[name] = value

        return result

    def search(
        self, 
        source: Optional[Path] = None, 
        sink: Optional[Path] = None, 
        exclude: Set[Edge] = None, 
        comparitive_operator: ComparitiveOperationEnum = ComparitiveOperationEnum.Equal
    ) -> List[Edge]:

        def compare(path1: Path, path2: Path):
            if comparitive_operator == ComparitiveOperationEnum.Equal:
                return path1 == path2 
            elif comparitive_operator == ComparitiveOperationEnum.Intersect:
                return iterables_intersect(path1.value, path2.value)

        def conditions(edge: Edge):
            if exclude and edge in exclude:
                return False 
            if source and not compare(edge.source, source):
                return False 
            if sink and not compare(edge.sink, sink):
                return False 
            return True

        return [edge for edge in self.edges if conditions(edge)]

    def create_subgraph(self, outputs: List[str]) -> Graph:
        frontier: List[Edge] = sum([self.search(sink=Path([output]), comparitive_operator=ComparitiveOperationEnum.Intersect) for output in outputs], [])
        edges: Set[Edge] = set()

        while frontier:
            edges = edges.union(set(frontier))
            frontier = sum([self.search(sink=fr_edge.source, comparitive_operator=ComparitiveOperationEnum.Equal, exclude=edges) for fr_edge in frontier], [])

        return self.__class__(edges=list(edges), outputs=outputs, event_handler=self.event_handler)

    def trigger_event(self, event_type: TraversalEventEnum, **kwargs):
        if handler := self.event_handler:
            event = Event(
                type=event_type, 
                graph_hash=hash(self), 
                traversal_id=self.traversal_id,
                payload=kwargs
            )
            handler(event)
            return True
        else:
            return False

class GraphFactory:
    default_event_handler: Optional[Callable] 

    def __init__(self, event_handler: Optional[Callable] = None):
        self.default_event_handler = event_handler

    def create(self, edges: List[Edge], event_handler: Optional[Callable] = None):
        return Graph(edges, event_handler=(event_handler or self.default_event_handler))
