from dataclasses import dataclass

from . import MasterNodeMemberInfo, MasterNodeIncentivePlan


@dataclass
class MasterNodeInfo:
    id: int
    addr: str
    creator: str
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
