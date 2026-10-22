from dataclasses import dataclass

from eth_typing import Address


@dataclass
class ProposalInfo:
    id: int
    creator: Address
    title: str
    payAmount: int
    payTimes: int
    startPayTime: int
    endPayTime: int
    description: str
    state: int
    createHeight: int
    updateHeight: int
