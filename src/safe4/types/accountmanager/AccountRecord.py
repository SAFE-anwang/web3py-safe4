from dataclasses import dataclass


@dataclass
class AccountRecord:
    id: int
    addr: str
    amount: int
    lockDay: int
    startHeight: int
    unlockHeight: int
