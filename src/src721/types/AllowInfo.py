from dataclasses import dataclass


@dataclass
class AllowInfo:
    addrs: list[str]
    amounts: list[int]
