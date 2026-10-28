from dataclasses import dataclass

from eth_typing import Address


@dataclass
class LockRecord:
    id: int
    addr: Address
    amount: int
    lockDay: int
    startHeight: int
    unlockHeight: int
