from dataclasses import dataclass


@dataclass
class ProposalInfo:
    id: int
    creator: str
    title: str
    payAmount: int
    payTimes: int
    startPayTime: int
    endPayTime: int
    description: str
    state: int
    createHeight: int
    updateHeight: int
