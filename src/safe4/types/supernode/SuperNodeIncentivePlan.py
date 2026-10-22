from dataclasses import dataclass


@dataclass
class SuperNodeIncentivePlan:
    creator: int
    partner: int
    voter: int
