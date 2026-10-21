from dataclasses import dataclass

from eth_typing import Address


@dataclass
class UnconfirmedPropertyInfo:
    name: str
    value: int
    applicant: Address
    voters: [Address]
    voteResults: [int]
    reason: str
    applyHeight: int
