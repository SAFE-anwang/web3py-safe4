from dataclasses import dataclass

from eth_typing import Address


@dataclass
class SNVoteRetInfo:
    addrs: list[Address]
    voteNums: list[int]
