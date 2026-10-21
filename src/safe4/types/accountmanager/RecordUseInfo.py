from dataclasses import dataclass

from eth_typing import Address


@dataclass
class RecordUseInfo:
    frozenAddr: Address
    freezeHeight: int
    unfreezeHeight: int
    votedAddr: Address
    voteHeight: int
    releaseHeight: int
