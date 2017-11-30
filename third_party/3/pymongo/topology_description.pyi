from typing import Callable, Dict, List, NamedTuple, Tuple, Union

from pymongo import common
from pymongo.read_preferences import ReadPreference, _ServerMode
from pymongo.server import Server
from pymongo.server_description import ServerDescription
from pymongo.server_selectors import Selection
from pymongo.server_type import SERVER_TYPE
from pymongo.settings import TopologySettings


class TopologyType(NamedTuple):
    Single: int
    ReplicaSetNoPrimary: int
    ReplicaSetWithPrimary: int
    Sharded: int
    Unknown: int
TOPOLOGY_TYPE: TopologyType = TopologyType(*range(5))
class TopologyDescription(object):
    def __init__(self,
                 topology_type: int,
                 server_descriptions: Dict[Tuple[str, int], ServerDescription],
                 replica_set_name: Union[str, None],
                 max_set_version: Union[int, None],
                 max_election_id: Union[int, None],
                 topology_settings: TopologySettings) -> None: ...
    def check_compatible(self) -> None: ...
    def has_server(self, address: Tuple[str, int]) -> bool: ...
    def reset_server(self, address: Tuple[str, int])\
        -> 'TopologyDescription': ...
    def reset(self) -> 'TopologyDescription': ...
    def server_descriptions(self)\
        -> Dict[Tuple[str, int], ServerDescription]: ...
    @property
    def topology_type(self) -> int: ...
    @property
    def topology_type_name(self) -> str: ...
    @property
    def replica_set_name(self) -> str: ...
    @property
    def max_set_version(self) -> int: ...
    @property
    def max_election_id(self) -> int: ...
    @property
    def known_servers(self) -> List[Server]: ...
    @property
    def common_wire_version(self) -> Union[int, None]: ...
    @property
    def heartbeat_frequency(self) -> int: ...
    def apply_selector(
        self,
        selector: Union[
            Selection, Callable[[Selection], Selection], _ServerMode],
        address: Tuple[str, int])\
        -> List[ServerDescription]: ...
    def has_readable_server(
        self,
        read_preference: _ServerMode = ReadPreference.PRIMARY) -> bool: ...
    def has_writable_server(self) -> bool: ...
_SERVER_TYPE_TO_TOPOLOGY_TYPE: Dict[int, int] = {
    SERVER_TYPE.Mongos: TOPOLOGY_TYPE.Sharded,
    SERVER_TYPE.RSPrimary: TOPOLOGY_TYPE.ReplicaSetWithPrimary,
    SERVER_TYPE.RSSecondary: TOPOLOGY_TYPE.ReplicaSetNoPrimary,
    SERVER_TYPE.RSArbiter: TOPOLOGY_TYPE.ReplicaSetNoPrimary,
    SERVER_TYPE.RSOther: TOPOLOGY_TYPE.ReplicaSetNoPrimary,
}
def updated_topology_description(
    topology_description: TopologyDescription,
    server_description: ServerDescription) -> TopologyDescription: ...
def _update_rs_from_primary(
    sds: Dict[Tuple[str, int], ServerDescription],
    replica_set_name: str,
    server_description: ServerDescription,
    max_set_version: int,
    max_election_id: int) -> Tuple[int, str, int, int]: ...
def _update_rs_with_primary_from_member(
    sds: Dict[Tuple[str, int], ServerDescription],
    replica_set_name: str,
    server_description: ServerDescription) -> int: ...
def _update_rs_no_primary_from_member(
    sds: Dict[Tuple[str, int], ServerDescription],
    replica_set_name: str,
    server_description: ServerDescription) -> Tuple[int, str]: ...
def _check_has_primary(sds: Dict[Tuple[str, int], ServerDescription])\
    -> int: ...
