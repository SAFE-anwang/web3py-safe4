from eth_typing import Address
from web3 import Web3

from ..types.accountmanager import AccountRecord, RecordUseInfo, AccountAmountInfo
from ..utils import Safe4ContractAddress, Safe4ContractABI, Safe4Contract


class AccountManager(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.AccountManagerContractAddr, Safe4ContractABI.AccountManagerABI)

    def deposit(self, privateKey: str, value: int, to: Address, lockDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="deposit", parameters=[to, lockDay])

    def batchDeposit4One(self, privateKey: str, value: int, to: Address, times: int, spaceDay: int,
                         startDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="batchDeposit4One",
                         parameters=[to, times, spaceDay, startDay])

    def batchDeposit4Multi(self, privateKey: str, value: int, addrs: list[Address], times: int, spaceDay: int,
                           startDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="batchDeposit4Multi",
                         parameters=[addrs, times, spaceDay, startDay])

    def withdrawByID(self, privateKey: str, ids: list[int]) -> str:
        return self.call(privateKey=privateKey, method="withdrawByID", parameters=[ids])

    def addLockDay(self, privateKey: str, id: int, day: int) -> str:
        return self.call(privateKey=privateKey, method="addLockDay", parameters=[id, day])

    def getImmatureAmount(self, addr: Address) -> int:
        return self.query(method="getImmatureAmount", parameters=[addr], outType=int)

    def getTotalAmount(self, addr: Address) -> AccountAmountInfo:
        return self.query(method="getTotalAmount", parameters=[addr], outType=AccountAmountInfo)

    def getTotalIDs(self, addr: Address, start: int, count: int) -> list[int]:
        return self.query(method="getTotalIDs", parameters=[addr, start, count], outType=list[int])

    def getAvailableAmount(self, addr: Address) -> AccountAmountInfo:
        return self.query(method="getAvailableAmount", parameters=[addr], outType=AccountAmountInfo)

    def getAvailableIDs(self, addr: Address, start: int, count: int) -> list[int]:
        return self.query(method="getAvailableIDs", parameters=[addr, start, count], outType=list[int])

    def getLockedAmount(self, addr: Address) -> AccountAmountInfo:
        return self.query(method="getLockedAmount", parameters=[addr], outType=AccountAmountInfo)

    def getLockedIDs(self, addr: Address, start: int, count: int) -> list[int]:
        return self.query(method="getLockedIDs", parameters=[addr, start, count], outType=list[int])

    def getUsedAmount(self, addr: Address) -> AccountAmountInfo:
        return self.query(method="getUsedAmount", parameters=[addr], outType=AccountAmountInfo)

    def getUsedIDs(self, addr: Address, start: int, count: int) -> list[int]:
        return self.query(method="getUsedIDs", parameters=[addr, start, count], outType=list[int])

    def getRecord0(self, addr: Address) -> AccountRecord:
        return self.query(method="getRecord0", parameters=[addr], outType=AccountRecord)

    def getRecordByID(self, id: int) -> AccountRecord:
        return self.query(method="getRecordByID", parameters=[id], outType=AccountRecord)

    def getRecordUseInfo(self, id: int) -> RecordUseInfo:
        return self.query(method="getRecordUseInfo", parameters=[id], outType=RecordUseInfo)
