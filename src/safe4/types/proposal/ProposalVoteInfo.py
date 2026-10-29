from dataclasses import dataclass


@dataclass
class ProposalVoteInfo:
    voter: str
    voteResult: int
