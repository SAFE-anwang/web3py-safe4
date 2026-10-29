from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.snvote import VoteRecord, SNVoteRetInfo


class SNVote(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.SNVoteContractAddr, Safe4ContractABI.SNVoteABI)

    def voteOrApproval(self, privateKey: str, isVote: bool, dstAddr: str, recordIDs: list[int]) -> str:
        return self.call(privateKey=privateKey, method="voteOrApproval",
                         parameters=[isVote, Web3.to_checksum_address(dstAddr), recordIDs])

    def voteOrApprovalWithAmount(self, privateKey: str, value: int, isVote: bool, dstAddr: str) -> str:
        return self.call(privateKey=privateKey, value=value, method="voteOrApprovalWithAmount",
                         parameters=[isVote, Web3.to_checksum_address(dstAddr)])

    def removeVoteOrApproval(self, privateKey: str, recordIDs: list[int]) -> str:
        return self.call(privateKey=privateKey, method="removeVoteOrApproval", parameters=[recordIDs])

    def proxyVote(self, privateKey: str, snAddr: str) -> str:
        return self.call(privateKey=privateKey, method="proxyVote", parameters=[Web3.to_checksum_address(snAddr)])

    def getRecordByID(self, id: int) -> VoteRecord:
        return self.query(method="getRecordByID", parameters=[id], outType=VoteRecord)

    def getAmount4Voter(self, voterAddr: str) -> int:
        return self.query(method="getAmount4Voter", parameters=[Web3.to_checksum_address(voterAddr)], outType=int)

    def getVoteNum4Voter(self, voterAddr: str) -> int:
        return self.query(method="getVoteNum4Voter", parameters=[Web3.to_checksum_address(voterAddr)], outType=int)

    def getSNNum4Voter(self, voterAddr: str) -> int:
        return self.query(method="getSNNum4Voter", parameters=[Web3.to_checksum_address(voterAddr)], outType=int)

    def getSNs4Voter(self, voterAddr: str, start: int, count: int) -> SNVoteRetInfo:
        return self.query(method="getSNs4Voter", parameters=[Web3.to_checksum_address(voterAddr), start, count],
                          outType=SNVoteRetInfo)

    def getProxyNum4Voter(self, voterAddr: str) -> int:
        return self.query(method="getProxyNum4Voter", parameters=[Web3.to_checksum_address(voterAddr)], outType=int)

    def getProxies4Voter(self, voterAddr: str, start: int, count: int) -> SNVoteRetInfo:
        return self.query(method="getProxies4Voter", parameters=[Web3.to_checksum_address(voterAddr), start, count],
                          outType=SNVoteRetInfo)

    def getVotedIDNum4Voter(self, voterAddr: str) -> int:
        return self.query(method="getVotedIDNum4Voter", parameters=[Web3.to_checksum_address(voterAddr)], outType=int)

    def getVotedIDs4Voter(self, voterAddr: str, start: int, count: int) -> list[int]:
        return self.query(method="getVotedIDs4Voter", parameters=[Web3.to_checksum_address(voterAddr), start, count],
                          outType=list[int])

    def getProxiedIDNum4Voter(self, voterAddr: str) -> int:
        return self.query(method="getProxiedIDNum4Voter", parameters=[Web3.to_checksum_address(voterAddr)], outType=int)

    def getProxiedIDs4Voter(self, voterAddr: str, start: int, count: int) -> list[int]:
        return self.query(method="getProxiedIDs4Voter", parameters=[Web3.to_checksum_address(voterAddr), start, count],
                          outType=list[int])

    def getTotalAmount(self, addr: str) -> int:
        return self.query(method="getTotalAmount", parameters=[Web3.to_checksum_address(addr)], outType=int)

    def getTotalVoteNum(self, addr: str) -> int:
        return self.query(method="getTotalVoteNum", parameters=[Web3.to_checksum_address(addr)], outType=int)

    def getVoterNum(self, addr: str) -> int:
        return self.query(method="getVoterNum", parameters=[Web3.to_checksum_address(addr)], outType=int)

    def getVoters(self, addr: str, start: int, count: int) -> SNVoteRetInfo:
        return self.query(method="getVoters", parameters=[Web3.to_checksum_address(addr), start, count],
                          outType=SNVoteRetInfo)

    def getIDNum(self, addr: str) -> int:
        return self.query(method="getIDNum", parameters=[Web3.to_checksum_address(addr)], outType=int)

    def getIDs(self, addr: str, start: int, count: int) -> list[int]:
        return self.query(method="getIDs", parameters=[Web3.to_checksum_address(addr), start, count], outType=list[int])

    def getAllAmount(self) -> int:
        return self.query(method="getAllAmount", outType=int)

    def getAllVoteNum(self) -> int:
        return self.query(method="getAllVoteNum", outType=int)

    def getAllProxiedAmount(self) -> int:
        return self.query(method="getAllProxiedAmount", outType=int)

    def getAllProxiedVoteNum(self) -> int:
        return self.query(method="getAllProxiedVoteNum", outType=int)
