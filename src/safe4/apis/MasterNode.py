from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.masternode import MasterNodeInfo


class MasterNode:
    def __init__(self, w3: Web3):
        self.logicContract = Safe4Contract(w3, Safe4ContractAddress.MasterNodeLogicContractAddr,
                                           Safe4ContractABI.MasterNodeLogicABI)
        self.storageContract = Safe4Contract(w3, Safe4ContractAddress.MasterNodeStorageContractAddr,
                                             Safe4ContractABI.MasterNodeStorageABI)

    def register(self, privateKey: str, value: int, isUnion: bool, addr: str, lockDay: int, enode: str,
                 description: str, creatorIncentive: int, partnerIncentive: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="register",
                                       parameters=[isUnion, Web3.to_checksum_address(addr), lockDay, enode, description,
                                                   creatorIncentive,
                                                   partnerIncentive])

    def appendRegister(self, privateKey: str, value: int, addr: str, lockDay: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="appendRegister",
                                       parameters=[Web3.to_checksum_address(addr), lockDay])

    def turnRegister(self, privateKey: str, addr: str, lockID: int) -> str:
        return self.logicContract.call(privateKey=privateKey, method="turnRegister",
                                       parameters=[Web3.to_checksum_address(addr), lockID])

    def changeAddress(self, privateKey: str, addr: str, newAddr: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeAddress",
                                       parameters=[Web3.to_checksum_address(addr), Web3.to_checksum_address(newAddr)])

    def changeEnode(self, privateKey: str, addr: str, enode: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeEnode",
                                       parameters=[Web3.to_checksum_address(addr), enode])

    def changeEnodeByID(self, privateKey: str, id: int, enode: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeEnodeByID", parameters=[id, enode])

    def changeDescription(self, privateKey: str, addr: str, desciption: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeDescription",
                                       parameters=[Web3.to_checksum_address(addr), desciption])

    def changeDescriptionByID(self, privateKey: str, id: int, description: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeDescriptionByID",
                                       parameters=[id, description])

    def getInfo(self, addr: str) -> MasterNodeInfo:
        return self.storageContract.query(method="getInfo", parameters=[Web3.to_checksum_address(addr)],
                                          outType=MasterNodeInfo)

    def getInfoByID(self, id: int) -> MasterNodeInfo:
        return self.storageContract.query(method="getInfoByID", parameters=[id], outType=MasterNodeInfo)

    def getIDsByEnode(self, enode: str) -> list[int]:
        return self.storageContract.query(method="getIDsByEnode", parameters=[enode], outType=list[int])

    def getNext(self) -> str:
        return self.storageContract.query(method="getNext", outType=str)

    def getNum(self) -> int:
        return self.storageContract.query(method="getNum", outType=int)

    def getAll(self, start: int, count: int) -> list[str]:
        return self.storageContract.query(method="getAll", parameters=[start, count], outType=list[str])

    def getAddrNum4Creator(self, creator: str) -> int:
        return self.storageContract.query(method="getAddrNum4Creator", parameters=[Web3.to_checksum_address(creator)],
                                          outType=int)

    def getAddrs4Creator(self, creator: str, start: int, count: int) -> list[str]:
        return self.storageContract.query(method="getAddrs4Creator",
                                          parameters=[Web3.to_checksum_address(creator), start, count],
                                          outType=list[str])

    def getAddrNum4Partner(self, partner: str) -> int:
        return self.storageContract.query(method="getAddrNum4Partner", parameters=[Web3.to_checksum_address(partner)],
                                          outType=int)

    def getAddrs4Partner(self, partner: str, start: int, count: int) -> list[str]:
        return self.storageContract.query(method="getAddrs4Partner",
                                          parameters=[Web3.to_checksum_address(partner), start, count],
                                          outType=list[str])

    def getOfficials(self) -> list[str]:
        return self.storageContract.query(method="getOfficials", outType=list[str])

    def exist(self, addr: str) -> bool:
        return self.storageContract.query(method="exist", parameters=[Web3.to_checksum_address(addr)], outType=bool)

    def existID(self, id: int) -> bool:
        return self.storageContract.query(method="existID", parameters=[id], outType=bool)

    def existEnode(self, enode: str) -> bool:
        return self.storageContract.query(method="existEnode", parameters=[enode], outType=bool)

    def existLockID(self, lockID: int) -> bool:
        return self.storageContract.query(method="existLockID", parameters=[lockID], outType=bool)

    def existFounder(self, founder: str) -> bool:
        return self.storageContract.query(method="existFounder", parameters=[Web3.to_checksum_address(founder)],
                                          outType=bool)

    def isValid(self, addr: str) -> bool:
        return self.storageContract.query(method="isValid", parameters=[Web3.to_checksum_address(addr)], outType=bool)

    def isUnion(self, addr: str) -> bool:
        return self.storageContract.query(method="isUnion", parameters=[Web3.to_checksum_address(addr)], outType=bool)

    def existNodeAddress(self, addr: str) -> bool:
        return self.storageContract.query(method="existNodeAddress", parameters=[Web3.to_checksum_address(addr)],
                                          outType=bool)

    def existNodeEnode(self, enode: str) -> bool:
        return self.storageContract.query(method="existNodeEnode", parameters=[enode], outType=bool)

    def existNodeFounder(self, founder: str) -> bool:
        return self.storageContract.query(method="existNodeFounder", parameters=[Web3.to_checksum_address(founder)],
                                          outType=bool)

    def isBindEnode(self, id: int, enode: str) -> bool:
        return self.storageContract.query(method="isBindEnode", parameters=[id, enode], outType=bool)

    def isValidEnode(self, enode: str) -> bool:
        return self.storageContract.query(method="isValidEnode", parameters=[enode], outType=bool)
