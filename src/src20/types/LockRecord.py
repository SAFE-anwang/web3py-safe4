from dataclasses import dataclass


@dataclass
class LockRecord:
    id: int
    addr: str
    amount: int
    lockDay: int
    startHeight: int
    unlockHeight: int
