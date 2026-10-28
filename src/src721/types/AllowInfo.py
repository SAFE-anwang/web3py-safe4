from dataclasses import dataclass

from eth_typing import Address


@dataclass
class AllowInfo:
    addrs: list[Address]
    amounts: list[int]
