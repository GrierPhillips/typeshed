from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

from pymongo.server_description import ServerDescription
from pymongo.server_selectors import Selection

_PRIMARY: int = 0
_PRIMARY_PREFERRED: int = 1
_SECONDARY: int = 2
_SECONDARY_PREFERRED: int = 3
_NEAREST: int = 4
_MONGOS_MODES: Tuple[str, ...] = (
    'primary',
    'primaryPreferred',
    'secondary',
    'secondaryPreferred',
    'nearest',
)
def _validate_tag_sets(tag_sets: Union[List[Mapping[str, Any]], None])\
    -> Union[List[Mapping[str, Any]], None]: ...
def _invalid_max_staleness_msg(max_staleness: int) -> str: ...
def _validate_max_staleness(max_staleness: int) -> int: ...
class _ServerMode(object):
    def __init__(self, mode: int,
                 tag_sets: Optional[List[Mapping[str, Any]]] = None,
                 max_staleness: int = -1) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def document(self) -> Dict[str, Union[str, List[Dict[str, Any]], int]]: ...
    @property
    def mode(self) -> int: ...
    @property
    def tag_sets(self) -> List[Dict[Any, Any]]: ...
    @property
    def max_staleness(self) -> int: ...
    @property
    def min_wire_version(self) -> int: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __getstate__(self) -> Dict[str, Union[int, List[Dict[Any, Any]]]]: ...
    def __setstate__(self, value: Dict[str, Union[int, List[Dict[Any, Any]]]])\
        -> None: ...
class Primary(_ServerMode):
    def __init__(self) -> None: ...
    def __call__(self, selection: Selection) -> List[ServerDescription]: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
class PrimaryPreferred(_ServerMode):
    def __init__(self, tag_sets: Optional[List[Dict[str, Any]]] = None,
                 max_staleness: int = -1) -> None: ...
    def __call__(self, selection: Selection)\
        -> Union[List[ServerDescription], Selection]: ...
class Secondary(_ServerMode):
    def __init__(self, tag_sets: Optional[List[Dict[str, Any]]] = None,
                 max_staleness: int = -1) -> None: ...
    def __call__(self, selection: Selection) -> Selection: ...
class SecondaryPreferred(_ServerMode):
    def __init__(self, tag_sets: Optional[List[Dict[str, Any]]] = None,
                 max_staleness: int = -1) -> None: ...
    def __call__(self, selection: Selection)\
        -> Union[List[ServerDescription], Selection]: ...
class Nearest(_ServerMode):
    def __init__(self, tag_sets: Optional[List[Dict[str, Any]]] = None,
                 max_staleness: int = -1) -> None: ...
    def __call__(self, selection: Selection) -> Selection: ...
def make_read_preference(mode: int, tag_sets: List[Dict[str, Any]],
                         max_staleness: int = -1) -> _ServerMode: ...
_MODES: Tuple[str, ...] = (
    'PRIMARY',
    'PRIMARY_PREFERRED',
    'SECONDARY',
    'SECONDARY_PREFERRED',
    'NEAREST',
)
class ReadPreference(object):
    PRIMARY: _ServerMode = Primary()
    PRIMARY_PREFERRED: _ServerMode = PrimaryPreferred()
    SECONDARY: _ServerMode = Secondary()
    SECONDARY_PREFERRED: _ServerMode = SecondaryPreferred()
    NEAREST: _ServerMode = Nearest()
def read_pref_mode_from_name(name: str) -> int: ...
class MovingAverage(object):
    def __init__(self) -> None: ...
    def add_sample(self, sample: int) -> None: ...
    def get(self) -> Union[float, None]: ...
    def reset(self) -> None: ...
