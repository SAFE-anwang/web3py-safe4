from dataclasses import dataclass

from eth_typing import Address


@dataclass
class DAppInfo:
    id: int
    name: str
    contractAddr: Address
    runUrl: str
    gitUrl: str
    officialUrl: str
    officialEmail: str
    officialAccount: Address
    description: str
    keyword: str
    fraudNum: int
    isFrozen: bool
