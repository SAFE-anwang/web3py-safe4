from dataclasses import dataclass

from eth_typing import Address


@dataclass
class MasterNodeMemberInfo:
    lockId: int
    addr: Address
    amount: int
    unlockHeight: int
