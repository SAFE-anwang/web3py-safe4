from dataclasses import dataclass

from eth_typing import Address


@dataclass
class VoteRecord:
    voterAddr: Address
    dstAddr: Address
    amount: int
    num: int
    height: int
