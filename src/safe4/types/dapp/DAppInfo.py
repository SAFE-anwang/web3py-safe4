from dataclasses import dataclass


@dataclass
class DAppInfo:
    id: int
    name: str
    contractAddr: str
    runUrl: str
    gitUrl: str
    officialUrl: str
    officialEmail: str
    officialAccount: str
    description: str
    keyword: str
    fraudNum: int
    isFrozen: bool
