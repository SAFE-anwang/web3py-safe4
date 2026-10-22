from eth_typing import Address
from web3 import Web3

from ..types.proposal import ProposalInfo, ProposalVoteInfo
from ..utils import Safe4ContractAddress, Safe4ContractABI, Safe4Contract


class Proposal(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.ProposalContractAddr, Safe4ContractABI.ProposalABI)

    def getBalance(self) -> int:
        return self.query(method="getBalance", outType=int)

    def getImmatureBalance(self) -> int:
        return self.query(method="getImmatureBalance", outType=int)

    def create(self, privateKey: str, title: str, payAmount: int, payTime: int, startPayTime: int, endPayTime: int,
               description: str) -> str:
        return self.call(privateKey=privateKey, value=10 ** 18, method="create",
                         parameters=[title, payAmount, payTime, startPayTime, endPayTime, description])

    def vote(self, privateKey: str, id: int, voteResult: int) -> str:
        return self.call(privateKey=privateKey, method="vote", parameters=[id, voteResult])

    def changeTitle(self, privateKey: str, id: int, title: str) -> str:
        return self.call(privateKey=privateKey, method="changeTitle", parameters=[id, title])

    def changePayAmount(self, privateKey: str, id: int, payAmount: int) -> str:
        return self.call(privateKey=privateKey, method="changePayAmount", parameters=[id, payAmount])

    def changePayTimes(self, privateKey: str, id: int, payTimes: int) -> str:
        return self.call(privateKey=privateKey, method="changePayTimes", parameters=[id, payTimes])

    def changeStartPayTime(self, privateKey: str, id: int, startPayTime: int) -> str:
        return self.call(privateKey=privateKey, method="changeStartPayTime", parameters=[id, startPayTime])

    def changeEndPayTime(self, privateKey: str, id: int, endPayTime: int) -> str:
        return self.call(privateKey=privateKey, method="changeEndPayTime", parameters=[id, endPayTime])

    def changeDescription(self, privateKey: str, id: int, description: str) -> str:
        return self.call(privateKey=privateKey, method="changeDescription", parameters=[id, description])

    def getInfo(self, id: int) -> ProposalInfo:
        return self.query(method="getInfo", parameters=[id], outType=ProposalInfo)

    def getVoterNum(self, id: int) -> int:
        return self.query(method="getVoterNum", parameters=[id], outType=int)

    def getVoteInfo(self, id: int, start: int, count: int) -> list[ProposalVoteInfo]:
        return self.query(method="getVoteInfo", parameters=[id, start, count], outType=list[ProposalVoteInfo])

    def getRewardIDs(self, id: int) -> list[int]:
        return self.query(method="getRewardIDs", parameters=[int], outType=list[int])

    def getNum(self) -> int:
        return self.query(method="getNum", outType=int)

    def getAll(self, start: int, count: int) -> list[int]:
        return self.query(method="getAll", parameters=[start, count], outType=list[int])

    def getMineNum(self, creator: Address) -> int:
        return self.query(method="getMineNum", parameters=[creator], outType=int)

    def getMines(self, creator: Address, start: int, count: int) -> list[int]:
        return self.query(method="getMines", parameters=[creator, start, count], outType=list[int])

    def exist(self, id: int) -> bool:
        return self.query(method="exist", parameters=[id], outType=bool)
