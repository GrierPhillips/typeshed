from socket import socket
import struct
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

from bson import CodecOptions
from pymongo.collation import Collation
from pymongo.common import MAX_MESSAGE_SIZE
from pymongo.monitoring import _EventListeners
from pymongo.read_concern import DEFAULT_READ_CONCERN, ReadConcern
from pymongo.read_preferences import _ServerMode


def command(sock: socket, dbname: str, spec: Mapping[str, Any], slave_ok: bool,
            is_mongos: bool, read_preference: _ServerMode,
            codec_options: CodecOptions, check: bool = True,
            allowable_errors: Optional[List[str]] = None,
            address: Optional[Tuple[str, int]] = None,
            check_keys: bool = False,
            listeners: Optional[_EventListeners] = None,
            max_bson_size: Optional[int] = None,
            read_concern: ReadConcern = DEFAULT_READ_CONCERN,
            parse_write_concern_error: bool = False,
            collation: Optional[Collation] = None) -> Dict[str, Any]: ...
def receive_message(
        sock: socket, operation: int, request_id: int,
        max_message_size: int = MAX_MESSAGE_SIZE) -> bytes: ...
def _receive_data_on_socket(sock: socket, length: int) -> bytes: ...
def _errno_from_exception(exc: Exception) -> Union[int, str, None]: ...
class SocketChecker(object):
    def __init__(self) -> None: ...
    def socket_closed(self, sock: socket) -> bool: ...
