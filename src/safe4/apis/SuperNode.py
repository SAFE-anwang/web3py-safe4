from eth_typing import Address
from web3 import Web3

from ..types.supernode import SuperNodeInfo
from ..utils import Safe4ContractAddress, Safe4ContractABI, Safe4Contract


class SuperNode:
    def __init__(self, w3: Web3):
        self.logicContract = Safe4Contract(w3, Safe4ContractAddress.SuperNodeLogicContractAddr,
                                           Safe4ContractABI.SuperNodeLogicABI)
        self.storageContract = Safe4Contract(w3, Safe4ContractAddress.SuperNodeStorageContractAddr,
                                             Safe4ContractABI.SuperNodeStorageABI)

    def register(self, privateKey: str, value: int, isUnion: bool, addr: Address, lockDay: int, name: str, enode: str,
                 description: str, creatorIncentive: int, partnerIncentive: int, voterIncentive: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="register",
                                       parameters=[isUnion, addr, lockDay, name, enode, description, creatorIncentive,
                                                   partnerIncentive, voterIncentive])

    def appendRegister(self, privateKey: str, value: int, addr: Address, lockDay: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="appendRegister",
                                       parameters=[addr, lockDay])

    def turnRegister(self, privateKey: str, addr: Address, lockID: int) -> str:
        return self.logicContract.call(privateKey=privateKey, method="turnRegister", parameters=[addr, lockID])

    def changeAddress(self, privateKey: str, addr: Address, newAddr: Address) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeAddress", parameters=[addr, newAddr])

    def changeName(self, privateKey: str, addr: Address, name: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeName", parameters=[addr, name])

    def changeNameByID(self, privateKey: str, id: int, name: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeNameByID", parameters=[id, name])

    def changeEnode(self, privateKey: str, addr: Address, enode: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeEnode", parameters=[addr, enode])

    def changeEnodeByID(self, privateKey: str, id: int, enode: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeEnodeByID", parameters=[id, enode])

    def changeDescription(self, privateKey: str, addr: Address, desciption: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeDescription", parameters=[addr, desciption])

    def changeDescriptionByID(self, privateKey: str, id: int, description: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeDescriptionByID",
                                       parameters=[id, description])

    def changeIncentivePlan(self, privateKey: str, id: int, creatorIncentive: int, partnerIncentive: int, voterIncentive: int) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeIncentivePlan", parameters=[id, creatorIncentive, partnerIncentive, voterIncentive])

    def getInfo(self, addr: Address) -> SuperNodeInfo:
        return self.storageContract.query(method="getInfo", parameters=[addr], outType=SuperNodeInfo)

    def getInfoByID(self, id: int) -> SuperNodeInfo:
        return self.storageContract.query(method="getInfoByID", parameters=[id], outType=SuperNodeInfo)

    def getDisableHeight(self, id: int) -> int:
        return self.storageContract.query(method="getDisableHeight", parameters=[id], outType=int)

    def getNum(self) -> int:
        return self.storageContract.query(method="getNum", outType=int)

    def getAll(self, start: int, count: int) -> list[Address]:
        return self.storageContract.query(method="getAll", parameters=[start, count], outType=list[Address])

    def getAddrNum4Creator(self, creator: Address) -> int:
        return self.storageContract.query(method="getAddrNum4Creator", parameters=[creator], outType=int)

    def getAddrs4Creator(self, creator: Address, start: int, count: int) -> list[Address]:
        return self.storageContract.query(method="getAddrs4Creator", parameters=[creator, start, count],
                                          outType=list[Address])

    def getAddrNum4Partner(self, partner: Address) -> int:
        return self.storageContract.query(method="getAddrNum4Partner", parameters=[partner], outType=int)

    def getAddrs4Partner(self, partner: Address, start: int, count: int) -> list[Address]:
        return self.storageContract.query(method="getAddrs4Partner", parameters=[partner, start, count],
                                          outType=list[Address])

    def getTops(self) -> list[Address]:
        return self.storageContract.query(method="getTops", outType=list[Address])

    def getTops4Creator(self, creator: Address) -> list[Address]:
        return self.storageContract.query(method="getTops4Creator", parameters=[creator], outType=list[Address])

    def getOfficials(self) -> list[Address]:
        return self.storageContract.query(method="getOfficials", outType=list[Address])

    def exist(self, addr: Address) -> bool:
        return self.storageContract.query(method="exist", parameters=[addr], outType=bool)

    def existID(self, id: int) -> bool:
        return self.storageContract.query(method="existID", parameters=[id], outType=bool)

    def existEnode(self, enode: str) -> bool:
        return self.storageContract.query(method="existEnode", parameters=[enode], outType=bool)

    def existLockID(self, lockID: int) -> bool:
        return self.storageContract.query(method="existLockID", parameters=[lockID], outType=bool)

    def existFounder(self, founder: Address) -> bool:
        return self.storageContract.query(method="existFounder", parameters=[founder], outType=bool)

    def isValid(self, addr: Address) -> bool:
        return self.storageContract.query(method="isValid", parameters=[addr], outType=bool)

    def isUnion(self, addr: Address) -> bool:
        return self.storageContract.query(method="isUnion", parameters=[addr], outType=bool)

    def existNodeAddress(self, addr: Address) -> bool:
        return self.storageContract.query(method="existNodeAddress", parameters=[addr], outType=bool)

    def existNodeEnode(self, enode: str) -> bool:
        return self.storageContract.query(method="existNodeEnode", parameters=[enode], outType=bool)

    def existNodeFounder(self, founder: Address) -> bool:
        return self.storageContract.query(method="existNodeFounder", parameters=[founder], outType=bool)
