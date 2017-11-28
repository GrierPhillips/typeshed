import collections
import datetime
from typing import Any, Callable, Dict, FrozenSet, List, Tuple, Union

from bson.binary import (STANDARD, PYTHON_LEGACY,
                         JAVA_LEGACY, CSHARP_LEGACY)
from bson.codec_options import CodecOptions
from bson.raw_bson import RawBSONDocument
from pymongo.monitoring import _validate_event_listeners
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import _ServerMode
from pymongo.ssl_support import validate_cert_reqs
from pymongo.write_concern import WriteConcern

MAX_BSON_SIZE: int = 16 * (1024 ** 2)
MAX_MESSAGE_SIZE: int = 2 * MAX_BSON_SIZE
MIN_WIRE_VERSION: int = 0
MAX_WIRE_VERSION: int = 0
MAX_WRITE_BATCH_SIZE: int = 1000
MIN_SUPPORTED_WIRE_VERSION: int = 0
MAX_SUPPORTED_WIRE_VERSION: int = 5
HEARTBEAT_FREQUENCY: int = 10
KILL_CURSOR_FREQUENCY: int = 1
EVENTS_QUEUE_FREQUENCY: int = 1
SERVER_SELECTION_TIMEOUT: int = 30
MIN_HEARTBEAT_INTERVAL: float = 0.5
CONNECT_TIMEOUT: float = 20.0
MAX_POOL_SIZE: int = 100
MIN_POOL_SIZE: int = 0
MAX_IDLE_TIME_MS: Union[int, None] = None
LOCAL_THRESHOLD_MS: int = 15
COMMAND_NOT_FOUND_CODES: Tuple[int, int, None] = (59, 13390, None)
UNAUTHORIZED_CODES: Tuple[int, int, int] = (13, 16547, 16548)
_UUID_REPRESENTATIONS: Dict[str, int] = {
    'standard': STANDARD,
    'pythonLegacy': PYTHON_LEGACY,
    'javaLegacy': JAVA_LEGACY,
    'csharpLegacy': CSHARP_LEGACY
}
_MECHANISM_PROPS: FrozenSet[str] = frozenset(['SERVICE_NAME',
                                              'CANONICALIZE_HOST_NAME',
                                              'SERVICE_REALM'])
_UNICODE_DECODE_ERROR_HANDLERS: FrozenSet[str] = frozenset(
    ['strict', 'replace', 'ignore'])
WRITE_CONCERN_OPTIONS: FrozenSet[str] = frozenset([
    'w',
    'wtimeout',
    'wtimeoutms',
    'fsync',
    'j',
    'journal'
])
def partition_node(node: str) -> Tuple[str, int]: ...
def clean_node(node: str) -> Tuple[str, int]: ...
def raise_config_error(key: str, dummy: Any) -> None: ...
def validate_boolean(option: str, value: Any) -> bool: ...
def validate_boolean_or_string(option: str, value: Any) -> bool: ...
def validate_integer(option: str, value: Any) -> int: ...
def validate_positive_integer(option: str, value: Any) -> int: ...
def validate_non_negative_integer(option: str, value: Any) -> int: ...
def validate_readable(option: str, value: Any) -> Union[str, None]: ...
def validate_positive_integer_or_none(option: str, value: Any) -> Union[int, None]: ...
def validate_non_negative_integer_or_none(option: str, value: Any) -> Union[int, None]: ...
def validate_string(option: str, value: Any) -> str: ...
def validate_string_or_none(option: str, value: Any) -> Union[str, None]: ...
def validate_int_or_basestring(option: str, value: Any) -> Union[int, str]: ...
def validate_positive_float(option: str, value: Any) -> float: ...
def validate_positive_float_or_zero(option: str, value: Any) -> Union[int, float]: ...
def validate_timeout_or_none(option: str, value: Any) -> Union[None, float]: ...
def validate_timeout_or_zero(option: str, value: Any) -> Union[int, float]: ...
def validate_max_staleness(option: str, value: Any) -> int: ...
def validate_read_preference(dummy: Any, value: Any) -> _ServerMode: ...
def validate_read_preference_mode(dummy: Any, value: Any) -> _ServerMode: ...
def validate_auth_mechanism(option: str, value: Any) -> str: ...
def validate_uuid_representation(dummy: Any, value: Any) -> int: ...
def validate_read_preference_tags(name: str, value: Any) -> List[Dict[str, str]]: ...
def validate_auth_mechanism_properties(option: str, value: Any) -> Dict[str, Union[bool, str]]: ...
def validate_document_class(
    option: str,
    value: Any) -> Union[collections.MutableMapping, RawBSONDocument]: ...
def validate_list(option: str, value: Any) -> List[Any]: ...
def validate_is_mapping(option: str, value: Any) -> Dict[Any, Any]: ...
def validate_is_document_type(option: str, value: Any) -> None: ...
def validate_appname_or_none(option: str, value: Any) -> Union[str, None]: ...
def validate_ok_for_replace(replacement: Any) -> None: ...
def validate_ok_for_update(update: Any) -> None: ...
def validate_unicode_decode_error_handler(dummy: Any, value: str) -> str: ...
def validate_tzinfo(dummy: Any, value: Any) -> Union[datetime.tzinfo, None]: ...
URI_VALIDATORS: Dict[str, Callable[..., Any]] = {
    'replicaset': validate_string_or_none,
    'w': validate_int_or_basestring,
    'wtimeout': validate_integer,
    'wtimeoutms': validate_integer,
    'fsync': validate_boolean_or_string,
    'j': validate_boolean_or_string,
    'journal': validate_boolean_or_string,
    'maxpoolsize': validate_positive_integer_or_none,
    'socketkeepalive': validate_boolean_or_string,
    'waitqueuemultiple': validate_non_negative_integer_or_none,
    'ssl': validate_boolean_or_string,
    'ssl_keyfile': validate_readable,
    'ssl_certfile': validate_readable,
    'ssl_pem_passphrase': validate_string_or_none,
    'ssl_cert_reqs': validate_cert_reqs,
    'ssl_ca_certs': validate_readable,
    'ssl_match_hostname': validate_boolean_or_string,
    'ssl_crlfile': validate_readable,
    'readconcernlevel': validate_string_or_none,
    'readpreference': validate_read_preference_mode,
    'readpreferencetags': validate_read_preference_tags,
    'localthresholdms': validate_positive_float_or_zero,
    'authmechanism': validate_auth_mechanism,
    'authsource': validate_string,
    'authmechanismproperties': validate_auth_mechanism_properties,
    'tz_aware': validate_boolean_or_string,
    'uuidrepresentation': validate_uuid_representation,
    'connect': validate_boolean_or_string,
    'minpoolsize': validate_non_negative_integer,
    'appname': validate_appname_or_none,
    'unicode_decode_error_handler': validate_unicode_decode_error_handler
}
TIMEOUT_VALIDATORS: Dict[str, Callable[..., Any]] = {
    'connecttimeoutms': validate_timeout_or_none,
    'sockettimeoutms': validate_timeout_or_none,
    'waitqueuetimeoutms': validate_timeout_or_none,
    'serverselectiontimeoutms': validate_timeout_or_zero,
    'heartbeatfrequencyms': validate_timeout_or_none,
    'maxidletimems': validate_timeout_or_none,
    'maxstalenessseconds': validate_max_staleness,
}
KW_VALIDATORS: Dict[str, Callable[..., Any]] = {
    'document_class': validate_document_class,
    'read_preference': validate_read_preference,
    'event_listeners': _validate_event_listeners,
    'tzinfo': validate_tzinfo
}
VALIDATORS: Dict[str, Callable[..., Any]] = URI_VALIDATORS.copy()
_AUTH_OPTIONS: FrozenSet[str] = frozenset(['authmechanismproperties'])
def validate_auth_option(option: str, value: Any) -> Tuple[str, Any]: ...
def validate(option: str, value: Any) -> Tuple[str, Any]: ...
def get_validated_options(options: Dict[str, Any],
                          warn: bool = True) -> Dict[str, Any]: ...
class BaseObject(object):
    def __init__(self, codec_options: CodecOptions,
                 read_preference: _ServerMode, write_concern: WriteConcern,
                 read_concern: ReadConcern) -> None: ...
    @property
    def codec_options(self) -> CodecOptions: ...
    @property
    def write_concern(self) -> WriteConcern: ...
    @property
    def read_preference(self) -> _ServerMode: ...
    @property
    def read_concern(self) -> ReadConcern: ...
