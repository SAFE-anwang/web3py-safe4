from dataclasses import dataclass

from . import SuperNodeMemberInfo, SuperNodeIncentivePlan


@dataclass
class SuperNodeInfo:
    id: int
    addr: str
    creator: str
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
