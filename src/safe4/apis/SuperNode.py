from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.supernode import SuperNodeInfo


class SuperNode:
    def __init__(self, w3: Web3):
        self.logicContract = Safe4Contract(w3, Safe4ContractAddress.SuperNodeLogicContractAddr,
                                           Safe4ContractABI.SuperNodeLogicABI)
        self.storageContract = Safe4Contract(w3, Safe4ContractAddress.SuperNodeStorageContractAddr,
                                             Safe4ContractABI.SuperNodeStorageABI)

    def register(self, privateKey: str, value: int, isUnion: bool, addr: str, lockDay: int, name: str, enode: str,
                 description: str, creatorIncentive: int, partnerIncentive: int, voterIncentive: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="register",
                                       parameters=[isUnion, Web3.to_checksum_address(addr), lockDay, name, enode,
                                                   description, creatorIncentive,
                                                   partnerIncentive, voterIncentive])

    def appendRegister(self, privateKey: str, value: int, addr: str, lockDay: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="appendRegister",
                                       parameters=[Web3.to_checksum_address(addr), lockDay])

    def turnRegister(self, privateKey: str, addr: str, lockID: int) -> str:
        return self.logicContract.call(privateKey=privateKey, method="turnRegister",
                                       parameters=[Web3.to_checksum_address(addr), lockID])

    def changeAddress(self, privateKey: str, addr: str, newAddr: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeAddress",
                                       parameters=[Web3.to_checksum_address(addr), Web3.to_checksum_address(newAddr)])

    def changeName(self, privateKey: str, addr: str, name: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeName",
                                       parameters=[Web3.to_checksum_address(addr), name])

    def changeNameByID(self, privateKey: str, id: int, name: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeNameByID", parameters=[id, name])

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

    def changeIncentivePlan(self, privateKey: str, id: int, creatorIncentive: int, partnerIncentive: int,
                            voterIncentive: int) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeIncentivePlan",
                                       parameters=[id, creatorIncentive, partnerIncentive, voterIncentive])

    def getInfo(self, addr: str) -> SuperNodeInfo:
        return self.storageContract.query(method="getInfo", parameters=[Web3.to_checksum_address(addr)],
                                          outType=SuperNodeInfo)

    def getInfoByID(self, id: int) -> SuperNodeInfo:
        return self.storageContract.query(method="getInfoByID", parameters=[id], outType=SuperNodeInfo)

    def getDisableHeight(self, id: int) -> int:
        return self.storageContract.query(method="getDisableHeight", parameters=[id], outType=int)

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

    def getTops(self) -> list[str]:
        return self.storageContract.query(method="getTops", outType=list[str])

    def getTops4Creator(self, creator: str) -> list[str]:
        return self.storageContract.query(method="getTops4Creator", parameters=[Web3.to_checksum_address(creator)],
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
