from dataclasses import dataclass


@dataclass
class MasterNodeMemberInfo:
    lockId: int
    addr: str
    amount: int
    unlockHeight: int
