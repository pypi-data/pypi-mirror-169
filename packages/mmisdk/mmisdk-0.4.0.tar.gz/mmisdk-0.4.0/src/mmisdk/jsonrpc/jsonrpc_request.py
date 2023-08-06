from typing import Generic, Optional, TypeVar, Union
from pydantic.generics import GenericModel

T = TypeVar("T")


class JsonRpcRequest(GenericModel, Generic[T]):
    jsonrpc = "2.0"
    method: str
    params: Optional[T]
    id: Optional[Union[str, int]]
