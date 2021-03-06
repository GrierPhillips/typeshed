import contextlib
from socket import socket
from ssl import SSLContext
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple, Union

from bson.codec_options import CodecOptions
from pymongo.auth import MongoCredential
from pymongo.collation import Collation
from pymongo.ismaster import IsMaster
from pymongo.monitoring import _EventListeners
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.write_concern import WriteConcern


def _raise_connection_failure(address: Tuple[str, int], error: Exception) -> None: ...
class PoolOptions(object):
    def __init__(self, max_pool_size: int = ..., min_pool_size: int = ..., max_idle_time_ms: Optional[int] = ..., connect_timeout: Optional[int] = ..., socket_timeout: Optional[int] = ..., wait_queue_timeout: Optional[int] = ..., wait_queue_multiple: Optional[int] = ..., ssl_context: Union[SSLContext, None] = ..., ssl_match_hostname: bool = ..., socket_keepalive: bool = ..., event_listeners: Optional[_EventListeners] = ..., appname: Optional[str] = ...) -> None: ...
    @property
    def max_pool_size(self) -> int: ...
    @property
    def min_pool_size(self) -> int: ...
    @property
    def max_idle_time_ms(self) -> int: ...
    @property
    def connect_timeout(self) -> int: ...
    @property
    def socket_timeout(self) -> int: ...
    @property
    def wait_queue_timeout(self) -> int: ...
    @property
    def wait_queue_multiple(self) -> int: ...
    @property
    def ssl_context(self) -> SSLContext: ...
    @property
    def ssl_match_hostname(self) -> bool: ...
    @property
    def socket_keepalive(self) -> bool: ...
    @property
    def event_listeners(self) -> _EventListeners: ...
    @property
    def appname(self) -> str: ...
    @property
    def metadata(self) -> Dict[str, Any]: ...

class SocketInfo(object):
    def __init__(self, sock: socket, pool: Pool, ismaster: IsMaster, address: Tuple[str, int]) -> None: ...
    def command(self, dbname: str, spec: Mapping[str, Any], slave_ok: bool = ..., read_preference: _ServerMode = ..., codec_options: CodecOptions = ..., check: bool = ..., allowable_errors: Optional[Sequence[str]] = ..., check_keys: bool = ..., read_concern: ReadConcern = ..., write_concern: Optional[WriteConcern] = ..., parse_write_concern_error: bool = ..., collation: Optional[Collation] = ...) -> Dict[str, MongoCredential]: ...
    def send_message(self, message: bytes, max_doc_size: int) -> None: ...
    def receive_message(self, operation: bytes, request_id: int) -> bytes: ...
    def legacy_write(self, request_id: int, msg: bytes, max_doc_size: int, with_last_error: bool) -> Dict[str, Any]: ...
    def write_command(self, request_id: int, msg: bytes) -> Dict[str, Any]: ...
    def check_auth(self, all_credentials: Mapping[str, MongoCredential]) -> None: ...
    def authenticate(self, credentials: MongoCredential) -> None: ...
    def close(self) -> None: ...
    def _raise_connection_failure(self, error: Exception) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...

def _create_connection(address: Tuple[str, int], options: PoolOptions) -> socket: ...
def _configured_socket(address: Tuple[str, int], options: PoolOptions) -> socket: ...

class Pool:
    def __init__(self, address: Tuple[str, int], options: PoolOptions, handshake: bool = ...) -> None: ...
    def reset(self) -> None: ...
    def remove_stale_sockets(self) -> None: ...
    def connect(self) -> SocketInfo: ...
    @contextlib.contextmanager
    def get_socket(self, all_credentials: Mapping[str, MongoCredential], checkout: bool = ...) -> SocketInfo: ...
    def _get_socket_no_auth(self) -> SocketInfo: ...
    def return_socket(self, sock_info: SocketInfo) -> None: ...
    def _check(self, sock_info: SocketInfo) -> SocketInfo: ...
    def _raise_wait_queue_timeout(self) -> None: ...
    def __del__(self) -> None: ...
