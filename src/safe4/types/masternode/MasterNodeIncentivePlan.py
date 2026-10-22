from dataclasses import dataclass


@dataclass
class MasterNodeIncentivePlan:
    creator: int
    partner: int
    voter: int
