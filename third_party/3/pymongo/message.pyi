import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

from bson import CodecOptions
from bson.son import SON
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.collation import Collation
from pymongo.monitoring import _EventListeners
from pymongo.pool import SocketInfo
from pymongo.read_concern import DEFAULT_READ_CONCERN, ReadConcern
from pymongo.read_preferences import _ServerMode

MAX_INT32: int = 2147483647
MIN_INT32: int = -2147483648
_COMMAND_OVERHEAD: int = 16382
_INSERT: int = 0
_UPDATE: int = 1
_DELETE: int = 2
_EMPTY: bytes = b''
_BSONOBJ: bytes = b'\x03'
_ZERO_8: bytes = b'\x00'
_ZERO_16: bytes = b'\x00\x00'
_ZERO_32: bytes = b'\x00\x00\x00\x00'
_ZERO_64: bytes = b'\x00\x00\x00\x00\x00\x00\x00\x00'
_SKIPLIM: bytes = b'\x00\x00\x00\x00\xff\xff\xff\xff'
_OP_MAP: Dict[int, bytes] = {
    _INSERT: b'\x04documents\x00\x00\x00\x00\x00',
    _UPDATE: b'\x04updates\x00\x00\x00\x00\x00',
    _DELETE: b'\x04deletes\x00\x00\x00\x00\x00',
}
_UJOIN: str = u"%s.%s"
def _randint() -> int: ...
def _maybe_add_read_preference(spec: SON, read_preference: _ServerMode)\
    -> SON: ...
def _convert_exception(exception: Exception) -> Dict[str, str]: ...
def _convert_write_result(
    operation: Union[_Query, _GetMore],
    command: Dict[str, Any],
    result: Dict[str, Any]) -> Dict[str, Any]: ...
_OPTIONS: SON = SON([
    ('tailable', 2),
    ('oplogReplay', 8),
    ('noCursorTimeout', 16),
    ('awaitData', 32),
    ('allowPartialResults', 128)])
_MODIFIERS: SON = SON([
    ('$query', 'filter'),
    ('$orderby', 'sort'),
    ('$hint', 'hint'),
    ('$comment', 'comment'),
    ('$maxScan', 'maxScan'),
    ('$maxTimeMS', 'maxTimeMS'),
    ('$max', 'max'),
    ('$min', 'min'),
    ('$returnKey', 'returnKey'),
    ('$showRecordId', 'showRecordId'),
    ('$showDiskLoc', 'showRecordId'),  # <= MongoDb 3.0
    ('$snapshot', 'snapshot')])
def _gen_explain_command(
    coll: Collection,
    spec: SON,
    projection: Union[Dict[str, bool], List[str]],
    skip: int,
    limit: int,
    batch_size: int,
    options: bool,
    read_concern: ReadConcern) -> SON: ...
def _gen_find_command(
    coll: Collection,
    spec: SON,
    projection: Union[Dict[str, bool], List[str]],
    skip: int,
    limit: int,
    batch_size: int,
    options: bool,
    read_concern: ReadConcern = DEFAULT_READ_CONCERN,
    collation: Optional[Collation] = None) -> SON: ...
def _gen_get_more_command(cursor_id: Any, coll: Collection, batch_size: int,
                          max_await_time_ms: int) -> SON: ...
class _Query(object):
    def __init__(self, flags: Any, db: Database, coll: Collection,
                 ntoskip: int, spec: Dict[str, Any], fields: Any,
                 codec_options: CodecOptions,
                 read_preference: _ServerMode,
                 limit: int, batch_size: int, read_concern: ReadConcern,
                 collation: Collation) -> None: ...
    def as_command(self) -> SON: ...
    def get_message(self, set_slave_ok: bool, is_mongos: bool,
                    use_cmd: bool = False) -> Tuple[int, bytes, int]: ...
class _GetMore(object):
    def __init__(self, db: Database, coll: Collection, ntoreturn: int,
                 cursor_id: Any, codec_options: CodecOptions,
                 max_await_time_ms: Optional[int] = None) -> None: ...
    def as_command(self) -> SON: ...
    def get_message(self, dummy0: Any, dummy1: Any,
                    use_cmd: bool = False) -> Tuple[Any]: ...
class _CursorAddress(tuple):
    def __new__(cls, address: Tuple[str, int],
                namespace: Any) -> '_CursorAddress': ...
    @property
    def namespace(self) -> Any: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
def __last_error(namespace: str, args: Dict[str, Any])\
    -> Tuple[int, bytes, int]: ...
def __pack_message(operation: Union[_Query, _GetMore], data: bytes)\
    -> Tuple[int, bytes]: ...
def insert(collection_name: str, docs: Dict[str, Any], check_keys: bool,
           safe: bool, last_error_args: Dict[str, Any],
           continue_on_error: bool, opts: CodecOptions)\
    -> Tuple[int, bytes, int]: ...
def update(collection_name: str, upsert: bool, multi: bool,
           spec: Dict[str, Any], doc: Dict[str, Any], safe: bool,
           last_error_args: Dict[str, Any], check_keys: bool,
           opts: CodecOptions) -> Tuple[int, bytes, int]: ...
def query(options: Any, collection_name: str, num_to_skip: int,
          num_to_return: int, query: Dict[str, Any], field_selector: Any,
          opts: CodecOptions, check_keys: bool = False)\
    -> Tuple[int, bytes, int]: ...
def get_more(collection_name: str, num_to_return: int, cursor_id: int)\
    -> Tuple[int, bytes]: ...
def delete(collection_name: str, spec: Dict[str, Any], safe: bool,
           last_error_args: Dict[str, Any], opts: CodecOptions,
           flags: int = 0) -> Tuple[int, bytes, int]: ...
def kill_cursors(cursor_ids: int) -> Tuple[int, bytes]: ...
_FIELD_MAP: Dict[str, str] = {
    'insert': 'documents',
    'update': 'updates',
    'delete': 'deletes'
}
class _BulkWriteContext(object):
    def __init__(self, database_name: str, command: Dict[str, Any],
                 sock_info: SocketInfo, operation_id: int,
                 listeners: _EventListeners) -> None: ...
    @property
    def max_bson_size(self) -> int: ...
    @property
    def max_message_size(self) -> int: ...
    @property
    def max_write_batch_size(self) -> int: ...
    def legacy_write(self, request_id: int, msg: bytes, max_doc_size: int,
                     acknowledged: bool, docs: Any) -> Dict[str, Any]: ...
    def write_command(self, request_id: int, msg: bytes,
                      docs: List[Dict[str, Any]]) -> Dict[str, Any]: ...
    def _start(self, request_id: int, docs: List[Dict[str, Any]])\
        -> Dict[str, Any]: ...
    def _succeed(self, request_id: int, reply: Dict[str, Any],
                 duration: datetime.timedelta) -> None: ...
    def _fail(self, request_id: int, failure: Dict[str, Any],
              duration: datetime.timedelta) -> None: ...
def _raise_document_too_large(operation: str, doc_size: int, max_size: int)\
    -> None: ...
def _do_batched_insert(collection_name: str, docs: List[Dict[str, Any]],
                       check_keys: bool, safe: bool,
                       last_error_args: Dict[str, Any],
                       continue_on_error: bool, opts: CodecOptions,
                       ctx: _BulkWriteContext) -> None: ...
def _do_batched_write_command(namespace: str, operation: int,
                              command: Dict[str, Any],
                              docs: List[Dict[str, Any]], check_keys: bool,
                              opts: CodecOptions, ctx: _BulkWriteContext)\
    -> None: ...
