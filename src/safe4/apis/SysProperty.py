from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.sysproperty import PropertyInfo, UnconfirmedPropertyInfo


class SysProperty(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.PropertyContractAddr, Safe4ContractABI.PropertyABI)

    def applyUpdate(self, privateKey: str, name: str, value: int, reason: str) -> str:
        return self.call(privateKey=privateKey, method="applyUpdate", parameters=[name, value, reason])

    def vote4Update(self, privateKey: str, name: str, voteResult: int) -> str:
        return self.call(privateKey=privateKey, method="vote4Update", parameters=[name, voteResult])

    def getInfo(self, name: str) -> PropertyInfo:
        return self.query(method="getInfo", parameters=[name], outType=PropertyInfo)

    def getUnconfirmedInfo(self, name: str) -> UnconfirmedPropertyInfo:
        return self.query(method="getUnconfirmedInfo", parameters=[name], outType=UnconfirmedPropertyInfo)

    def getValue(self, name: str) -> int:
        return self.query(method="getValue", parameters=[name], outType=int)

    def getNum(self) -> int:
        return self.query(method="getNum", outType=int)

    def getAll(self, start: int, count: int) -> list[str]:
        return self.query(method="getAll", parameters=[start, count], outType=list[str])

    def getUnconfirmedNum(self) -> int:
        return self.query(method="getUnconfirmedNum", outType=int)

    def getAllUnconfirmed(self, start: int, count: int) -> list[str]:
        return self.query(method="getAllUnconfirmed", parameters=[start, count], outType=list[str])

    def exist(self, name):
        return self.query(method="exist", parameters=[name], outType=bool)

    def existUnconfirmed(self, name):
        return self.query(method="existUnconfirmed", parameters=[name], outType=bool)
