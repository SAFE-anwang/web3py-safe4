from dataclasses import dataclass

from eth_typing import Address


@dataclass
class AvailableSafe3Info:
    safe3Addr: str
    amount: int
    safe4Addr: Address
    redeemHeight: int
