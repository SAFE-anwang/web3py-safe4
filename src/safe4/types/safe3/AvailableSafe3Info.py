from dataclasses import dataclass


@dataclass
class AvailableSafe3Info:
    safe3Addr: str
    amount: int
    safe4Addr: str
    redeemHeight: int
