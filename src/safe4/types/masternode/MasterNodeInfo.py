from dataclasses import dataclass

from eth_typing import Address

from . import MasterNodeMemberInfo, MasterNodeIncentivePlan


@dataclass
class MasterNodeInfo:
    id: int
    addr: Address
    creator: Address
    enode: str
    description: str
    isOfficial: bool
    state: int
    founders: list[MasterNodeMemberInfo]
    incentivePlan: MasterNodeIncentivePlan
    isUnion: bool
    lastRewardHeight: int
    createHeight: int
    updateHeight: int
