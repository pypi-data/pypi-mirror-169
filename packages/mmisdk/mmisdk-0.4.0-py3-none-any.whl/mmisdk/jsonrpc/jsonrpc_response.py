from typing import Generic, Optional, TypeVar, Union
from pydantic.generics import GenericModel
from mmisdk.jsonrpc.jsonrpc_error import JsonRpcError

T = TypeVar("T")


class JsonRpcResponse(GenericModel, Generic[T]):
    jsonrpc = "2.0"
    result: Optional[T]
    error: Optional[JsonRpcError]
    id: Optional[Union[str, int]]
