from dataclasses import dataclass

from eth_typing import Address


@dataclass
class SuperNodeMemberInfo:
    lockId: int
    addr: Address
    amount: int
    unlockHeight: int
