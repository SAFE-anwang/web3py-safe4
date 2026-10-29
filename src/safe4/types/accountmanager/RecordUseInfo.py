from dataclasses import dataclass


@dataclass
class RecordUseInfo:
    frozenAddr: str
    freezeHeight: int
    unfreezeHeight: int
    votedAddr: str
    voteHeight: int
    releaseHeight: int
