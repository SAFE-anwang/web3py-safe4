from dataclasses import dataclass

from eth_typing import Address


@dataclass
class LockedSafe3Info:
    safe3Addr: str
    amount: int
    remainLockHeight: int
    lockDay: int
    isMN: bool
    safe4Addr: Address
    redeemHeight: int
