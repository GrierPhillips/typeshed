from typing import Callable, List, Optional, Sequence, Set, Tuple, Union
if PY3:
    import queue as Queue
else:
    import Queue

from pymongo.pool import Pool
from pymongo.server import Server
from pymongo.server_description import ServerDescription
from pymongo.server_selectors import Selection
from pymongo.settings import TopologySettings


def process_events_queue(queue_ref: type) -> bool: ...
class Topology(object):
    """Monitor a topology of one or more servers."""
    def __init__(self, topology_settings: TopologySettings) -> None: ...
    def open(self) -> None: ...
    def select_servers(self,
                       selector: Callable[[Sequence[Server]], Sequence[Server]],
                       server_selection_timeout: Optional[int] = None,
                       address: Optional[Tuple[str, int]] = None)\
        -> List[Server]: ...
    def select_server(self,
                      selector: Callable[[Sequence[Server]], Sequence[Server]],
                      server_selection_timeout: Optional[int] = None,
                      address: Optional[Tuple[str, int]] = None)\
        -> Server: ...
    def select_server_by_address(
        self,
        address: Tuple[str, int],
        server_selection_timeout: Optional[int] = None) -> Server: ...
    def on_change(self, server_description: ServerDescription) -> None: ...
    def get_server_by_address(self, address: Tuple[str, int])\
        -> Union[Server, None]: ...
    def has_server(self, address: Tuple[str, int]) -> bool: ...
    def get_primary(self) -> Union[Tuple[str, int], None]: ...
    def _get_replica_set_members(
        self,
        selector: Callable[[Selection], List[ServerDescription]])\
        -> Set[Tuple[str, int]]: ...
    def get_secondaries(self) -> Set[Tuple[str, int]]: ...
    def get_arbiters(self) -> Set[Tuple[str, int]]: ...
    def request_check_all(self, wait_time: int = 5) -> None: ...
    def reset_pool(self, address: Tuple[str, int]) -> None: ...
    def reset_server(self, address: Tuple[str, int]) -> None: ...
    def reset_server_and_request_check(self, address: Tuple[str, int])\
        -> None: ...
    def update_pool(self) -> None: ...
    def close(self) -> None: ...
    @property
    def description(self) -> ServerDescription: ...
    def _new_selection(self) -> Selection: ...
    def _ensure_opened(self) -> None: ...
    def _reset_server(self, address: Tuple[str, int]) -> None: ...
    def _request_check(self, address: Tuple[str, int]) -> None: ...
    def _request_check_all(self) -> None: ...
    def _update_servers(self) -> None: ...
    def _create_pool_for_server(self, address: Tuple[str, int]) -> Pool: ...
    def _create_pool_for_monitor(self, address: Tuple[str, int]) -> Pool: ...
    def _error_message(self, selector: Callable[[Selection], Selection]) -> str: ...
