from typing import Any, Dict, List, Optional, Set, Tuple, Union

from bson import CodecOptions, SON
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.monitoring import _EventListeners
from pymongo.pool import SocketInfo
from pymongo.read_preferences import _ServerMode


_UUNDER: str = u"_"
_UNICODE_REPLACE_CODEC_OPTIONS: CodecOptions = CodecOptions(
    unicode_decode_error_handler='replace')
def _gen_index_name(keys: Union[List[str], Set[str]]) -> str: ...
def _index_list(key_or_list: Union[str, List[Tuple[str, Union[int, str]]]],
                direction: Optional[Union[int, str]] = None)\
    -> List[Tuple[str, Union[int, str]]]: ...
def _index_document(index_list: List[Tuple[str, Union[int, str]]]) -> SON: ...
def _unpack_response(
    response: bytes,
    cursor_id: Optional[int] = None,
    codec_options: CodecOptions = _UNICODE_REPLACE_CODEC_OPTIONS)\
    -> Dict[str, Any]: ...
def _check_command_response(response: bytes, msg: Optional[str] = None,
                            allowable_errors: Optional[List[str]] = None,
                            parse_write_concern_error: bool = False)\
    -> None: ...
def _check_gle_response(response: bytes) -> Dict[str, Any]: ...
def _first_batch(sock_info: SocketInfo, db: Database, coll: Collection,
                 query: Dict[str, Any], ntoreturn: int,
                 slave_ok: bool, codec_options: CodecOptions,
                 read_preference: _ServerMode, cmd: Dict[str, Any],
                 listeners: _EventListeners) -> Dict[str, Any]: ...
def _check_write_command_response(results: Dict[str, Any]) -> None: ...
def _fields_list_to_dict(fields: List[str], option_name: str)\
    -> Dict[str, int]: ...
