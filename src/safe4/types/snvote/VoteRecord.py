from dataclasses import dataclass


@dataclass
class VoteRecord:
    voterAddr: str
    dstAddr: str
    amount: int
    num: int
    height: int
