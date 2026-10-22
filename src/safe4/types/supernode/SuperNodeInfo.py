from dataclasses import dataclass

from eth_typing import Address

from . import SuperNodeMemberInfo, SuperNodeIncentivePlan


@dataclass
class SuperNodeInfo:
    id: int
    addr: Address
    creator: Address
    enode: str
    description: str
    isOfficial: bool
    state: int
    founders: list[SuperNodeMemberInfo]
    incentivePlan: SuperNodeIncentivePlan
    isUnion: bool
    lastRewardHeight: int
    createHeight: int
    updateHeight: int
