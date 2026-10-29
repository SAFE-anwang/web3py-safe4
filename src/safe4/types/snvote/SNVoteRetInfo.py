from dataclasses import dataclass


@dataclass
class SNVoteRetInfo:
    addrs: list[str]
    voteNums: list[int]
