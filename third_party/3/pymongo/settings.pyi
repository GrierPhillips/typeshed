import threading
from typing import Dict, List, Optional, Tuple

from pymongo.common import (HEARTBEAT_FREQUENCY, LOCAL_THRESHOLD_MS,
                            SERVER_SELECTION_TIMEOUT)
from pymongo.monitor import Monitor
from pymongo.pool import Pool, PoolOptions
from pymongo.server_description import ServerDescription


class TopologySettings(object):
    def __init__(self,
                 seeds: Optional[List[Tuple[str, int]]] = None,
                 replica_set_name: Optional[str] = None,
                 pool_class: Optional[Pool] = None,
                 pool_options: Optional[PoolOptions] = None,
                 monitor_class: Optional[Monitor] = None,
                 condition_class: Optional[threading.Condition] = None,
                 local_threshold_ms: int = LOCAL_THRESHOLD_MS,
                 server_selection_timeout: int = SERVER_SELECTION_TIMEOUT,
                 heartbeat_frequency: int = HEARTBEAT_FREQUENCY)\
        -> None: ...
    @property
    def seeds(self) -> List[Tuple[str, int]]: ...
    @property
    def replica_set_name(self) -> str: ...
    @property
    def pool_class(self) -> Pool: ...
    @property
    def pool_options(self) -> PoolOptions: ...
    @property
    def monitor_class(self) -> Monitor: ...
    @property
    def condition_class(self) -> threading.Condition: ...
    @property
    def local_threshold_ms(self) -> int: ...
    @property
    def server_selection_timeout(self) -> int: ...
    @property
    def heartbeat_frequency(self) -> int: ...
    @property
    def direct(self) -> bool: ...
    def get_topology_type(self) -> int: ...
    def get_server_descriptions(self)\
        -> Dict[Tuple[str, int], ServerDescription]: ...
