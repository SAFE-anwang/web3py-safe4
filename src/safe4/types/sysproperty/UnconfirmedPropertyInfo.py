from dataclasses import dataclass


@dataclass
class UnconfirmedPropertyInfo:
    name: str
    value: int
    applicant: str
    voters: list[str]
    voteResults: list[int]
    reason: str
    applyHeight: int
