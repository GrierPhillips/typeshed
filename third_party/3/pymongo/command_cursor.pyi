from typing import Any, Dict, Tuple, Union

from pymongo import message
from pymongo.collection import Collection


class CommandCursor(object):
    def __init__(self, collection: Collection, cursor_info: Dict[str, Any], address: Tuple[str, int], retrieved: int = ...) -> None: ...
    def __del__(self) -> None: ...
    def __die(self) -> None: ...
    def close(self) -> None: ...
    def batch_size(self, batch_size: int) -> 'CommandCursor': ...
    def __send_message(self, operation: Union[message._Query, message._GetMore]) -> None: ...
    def _refresh(self) -> int: ...
    @property
    def alive(self) -> bool: ...
    @property
    def cursor_id(self) -> int: ...
    @property
    def address(self) -> Tuple[str, int]: ...
    def __iter__(self) -> 'CommandCursor': ...
    def next(self) -> Dict[str, Any]: ...
    def __enter__(self) -> 'CommandCursor': ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
