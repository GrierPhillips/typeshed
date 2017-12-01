import contextlib
from typing import (Any, Callable, Dict, FrozenSet, List, Optional,
                    Set, Sequence, Tuple, Type, Union)

from bson import CodecOptions
from pymongo.auth import MongoCredential
from pymongo.common import BaseObject
from pymongo.cursor_manager import CursorManager
from pymongo.database import Database
from pymongo.message import _CursorAddress, _GetMore, _Query
from pymongo.monitoring import _EventListeners
from pymongo.pool import SocketInfo
from pymongo.topology import Topology
from pymongo.write_concern import WriteConcern
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.response import Response
from pymongo.server import Server

class MongoClient(BaseObject):
    HOST: str = ...
    PORT: int = ...
    def __init__(self, host: str = ..., port: int = ..., document_class: Type[Any] = ..., tz_aware: Optional[bool] = ..., connect: Optional[bool] = ..., **kwargs: Any) -> None: ...
    def _cache_credentials(self, source: str, credentials: MongoCredential, connect: bool = ...) -> None: ...
    def _purge_credentials(self, source: str) -> None: ...
    def _cached(self, dbname: str, coll: str, index: Union[str, int]) -> bool: ...
    def _cache_index(self, dbname: str, collection: str, index: Union[str, int], cache_for: int) -> None: ...
    def _purge_index(self, database_name: str, collection_name: Optional[str] = ..., index_name: Optional[str] = ...) -> None: ...
    def _server_property(self, attr_name: str) -> Any: ...
    @property
    def event_listeners(self) -> _EventListeners: ...
    @property
    def address(self) -> Union[Tuple[str, int], None]: ...
    @property
    def primary(self) -> Union[Tuple[str, int], None]: ...
    @property
    def secondaries(self) -> Union[Set[str], Set[Tuple[str, int]]]: ...
    @property
    def arbiters(self) -> Union[Set[str], Set[Tuple[str, int]]]: ...
    @property
    def is_primary(self) -> bool: ...
    @property
    def is_mongos(self) -> bool: ...
    @property
    def max_pool_size(self) -> int: ...
    @property
    def min_pool_size(self) -> int: ...
    @property
    def max_idle_time_ms(self) -> int: ...
    @property
    def nodes(self) -> FrozenSet[Tuple[str, int]]: ...
    @property
    def max_bson_size(self) -> int: ...
    @property
    def max_message_size(self) -> int: ...
    @property
    def max_write_batch_size(self) -> int: ...
    @property
    def local_threshold_ms(self) -> int: ...
    @property
    def server_selection_timeout(self) -> int: ...
    @property
    def _is_writable(self) -> bool: ...
    def close(self) -> None: ...
    def set_cursor_manager(self, manager_class: CursorManager) -> None: ...
    def _get_topology(self) -> Topology: ...
    @contextlib.contextmanager
    def _get_socket(self, selector: Callable[[Sequence[Server]], Sequence[Server]]) -> None: ...
    def _socket_for_writes(self) -> SocketInfo: ...
    @contextlib.contextmanager
    def _socket_for_reads(self, read_preference: _ServerMode) -> Tuple[SocketInfo, bool]: ...
    def _send_message_with_response(self, operation: Union[_Query, _GetMore], read_preference: Optional[_ServerMode] = ..., exhaust: bool = ..., address: Optional[Tuple[str, int]] = ...) -> Response: ...
    def _reset_on_error(self, server: Server, func: Callable[[Any], Any], *args: Any, **kwargs: Any) -> Any: ...
    def __reset_server(self, address: Tuple[str, int]) -> None: ...
    def _reset_server_and_request_check(self, address: Tuple[str, int]) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def _repr_helper(self) -> str: ...
    def __repr__(self) -> str: ...
    def __getattr__(self, name: str) -> Database: ...
    def __getitem__(self, name: str) -> Database: ...
    def close_cursor(self, cursor_id: int, address: Optional[Tuple[str, int]] = ...) -> None: ...
    def _close_cursor_now(self, cursor_id: int, address: Optional[Tuple[str, int]] = ...) -> None: ...
    def kill_cursors(self, cursor_ids: Sequence[int], address: Optional[Tuple[str, int]] = ...) -> None: ...
    def _kill_cursors(self, cursor_ids: Sequence[int], address: Union[Tuple[str, int], _CursorAddress], topology: Topology) -> None: ...
    def _process_periodic_tasks(self) -> None: ...
    def server_info(self) -> Dict[str, Any]: ...
    def database_names(self) -> List[str]: ...
    def drop_database(self, name_or_database: Union[str, Database]) -> None: ...
    def get_default_database(self) -> Database: ...
    def get_database(self, name: Optional[str] = ..., codec_options: Optional[CodecOptions] = ..., read_preference: Optional[_ServerMode] = ..., write_concern: Optional[WriteConcern] = ..., read_concern: Optional[ReadConcern] = ...) -> Database: ...
    def _database_default_options(self, name: str) -> Database: ...
    @property
    def is_locked(self) -> bool: ...
    def fsync(self, **kwargs: Any) -> Dict[str, Any]: ...
    def unlock(self) -> None: ...
    def __enter__(self) -> 'MongoClient': ...
    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
    def __iter__(self) -> 'MongoClient': ...
    def __next__(self) -> None: ...
