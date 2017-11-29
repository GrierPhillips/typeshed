from typing import Any, Dict, List, Tuple, Union


def _get_server_type(doc: Dict[str, Any]) -> int: ...
class IsMaster(object):
    def __init__(self, doc: Dict[str, Any]) -> None: ...
    @property
    def document(self) -> Dict[str, Any]: ...
    @property
    def server_type(self) -> int: ...
    @property
    def all_hosts(self) -> List[Any]: ...
    @property
    def tags(self) -> Dict[str, Any]: ...
    @property
    def primary(self) -> Union[Tuple[str, int], None]: ...
    @property
    def replica_set_name(self) -> Union[str, None]: ...
    @property
    def max_bson_size(self) -> int: ...
    @property
    def max_message_size(self) -> int: ...
    @property
    def max_write_batch_size(self) -> int: ...
    @property
    def min_wire_version(self) -> int: ...
    @property
    def max_wire_version(self) -> int: ...
    @property
    def set_version(self) -> Any: ...
    @property
    def election_id(self) -> Any: ...
    @property
    def is_writable(self) -> bool: ...
    @property
    def is_readable(self) -> bool: ...
    @property
    def me(self) -> Union[Tuple[str, int], None]: ...
    @property
    def last_write_date(self) -> Any: ...