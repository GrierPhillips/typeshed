from typing import NamedTuple

class SERVER_TYPE(NamedTuple):
    Unknown: int = 0
    Mongos: int = 1
    RSPrimary: int = 2
    RSSecondary: int = 3
    RSArbiter: int = 4
    RSOther: int = 5
    RSGhost: int = 6
    Standalone: int = 7
