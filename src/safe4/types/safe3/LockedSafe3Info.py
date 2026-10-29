from dataclasses import dataclass


@dataclass
class LockedSafe3Info:
    safe3Addr: str
    amount: int
    remainLockHeight: int
    lockDay: int
    isMN: bool
    safe4Addr: str
    redeemHeight: int
