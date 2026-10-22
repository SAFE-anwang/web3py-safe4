from eth_typing import Address
from web3 import Web3

from ..types.masternode import MasterNodeInfo
from ..utils import Safe4ContractAddress, Safe4ContractABI, Safe4Contract


class MasterNode:
    def __init__(self, w3: Web3):
        self.logicContract = Safe4Contract(w3, Safe4ContractAddress.MasterNodeLogicContractAddr,
                                           Safe4ContractABI.MasterNodeLogicABI)
        self.storageContract = Safe4Contract(w3, Safe4ContractAddress.MasterNodeStorageContractAddr,
                                             Safe4ContractABI.MasterNodeStorageABI)

    def register(self, privateKey: str, value: int, isUnion: bool, addr: Address, lockDay: int, enode: str,
                 description: str, creatorIncentive: int, partnerIncentive: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="register",
                                       parameters=[isUnion, addr, lockDay, enode, description, creatorIncentive,
                                                   partnerIncentive])

    def appendRegister(self, privateKey: str, value: int, addr: Address, lockDay: int) -> str:
        return self.logicContract.call(privateKey=privateKey, value=value, method="appendRegister",
                                       parameters=[addr, lockDay])

    def turnRegister(self, privateKey: str, addr: Address, lockID: int) -> str:
        return self.logicContract.call(privateKey=privateKey, method="turnRegister", parameters=[addr, lockID])

    def changeAddress(self, privateKey: str, addr: Address, newAddr: Address) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeAddress", parameters=[addr, newAddr])

    def changeEnode(self, privateKey: str, addr: Address, enode: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeEnode", parameters=[addr, enode])

    def changeEnodeByID(self, privateKey: str, id: int, enode: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeEnodeByID", parameters=[id, enode])

    def changeDescription(self, privateKey: str, addr: Address, desciption: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeDescription", parameters=[addr, desciption])

    def changeDescriptionByID(self, privateKey: str, id: int, description: str) -> str:
        return self.logicContract.call(privateKey=privateKey, method="changeDescriptionByID",
                                       parameters=[id, description])

    def getInfo(self, addr: Address) -> MasterNodeInfo:
        return self.storageContract.query(method="getInfo", parameters=[addr], outType=MasterNodeInfo)

    def getInfoByID(self, id: int) -> MasterNodeInfo:
        return self.storageContract.query(method="getInfoByID", parameters=[id], outType=MasterNodeInfo)

    def getIDsByEnode(self, enode: str) -> list[int]:
        return self.storageContract.query(method="getIDsByEnode", parameters=[enode], outType=list[int])

    def getNext(self) -> Address:
        return self.storageContract.query(method="getNext", outType=Address)

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

    def getOfficials(self) -> list[Address]:
        return self.storageContract.query(method="getOfficials", outType=list[Address])

    def exist(self, addr: Address) -> bool:
        return self.storageContract.query(method="exist", parameters=[addr], outType=bool)

    def existID(self, id: int) -> bool:
        return self.storageContract.query(method="existID", parameters=[id], outType=bool)
