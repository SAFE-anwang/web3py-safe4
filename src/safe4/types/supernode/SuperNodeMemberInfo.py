from dataclasses import dataclass


@dataclass
class SuperNodeMemberInfo:
    lockId: int
    addr: str
    amount: int
    unlockHeight: int
