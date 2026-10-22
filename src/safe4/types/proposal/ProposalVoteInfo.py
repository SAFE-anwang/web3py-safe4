from dataclasses import dataclass

from eth_typing import Address


@dataclass
class ProposalVoteInfo:
    voter: Address
    voteResult: int
