from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.accountmanager import AccountRecord, RecordUseInfo, AccountAmountInfo


class AccountManager(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.AccountManagerContractAddr, Safe4ContractABI.AccountManagerABI)

    def deposit(self, privateKey: str, value: int, to: str, lockDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="deposit",
                         parameters=[Web3.to_checksum_address(to), lockDay])

    def batchDeposit4One(self, privateKey: str, value: int, to: str, times: int, spaceDay: int,
                         startDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="batchDeposit4One",
                         parameters=[Web3.to_checksum_address(to), times, spaceDay, startDay])

    def batchDeposit4Multi(self, privateKey: str, value: int, addrs: list[str], times: int, spaceDay: int,
                           startDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="batchDeposit4Multi",
                         parameters=[[Web3.to_checksum_address(addr) for addr in addrs], times, spaceDay, startDay])

    def withdrawByID(self, privateKey: str, ids: list[int]) -> str:
        return self.call(privateKey=privateKey, method="withdrawByID", parameters=[ids])

    def addLockDay(self, privateKey: str, id: int, day: int) -> str:
        return self.call(privateKey=privateKey, method="addLockDay", parameters=[id, day])

    def getImmatureAmount(self, addr: str) -> int:
        return self.query(method="getImmatureAmount", parameters=[Web3.to_checksum_address(addr)], outType=int)

    def getTotalAmount(self, addr: str) -> AccountAmountInfo:
        return self.query(method="getTotalAmount", parameters=[Web3.to_checksum_address(addr)],
                          outType=AccountAmountInfo)

    def getTotalIDs(self, addr: str, start: int, count: int) -> list[int]:
        return self.query(method="getTotalIDs", parameters=[Web3.to_checksum_address(addr), start, count],
                          outType=list[int])

    def getAvailableAmount(self, addr: str) -> AccountAmountInfo:
        return self.query(method="getAvailableAmount", parameters=[Web3.to_checksum_address(addr)],
                          outType=AccountAmountInfo)

    def getAvailableIDs(self, addr: str, start: int, count: int) -> list[int]:
        return self.query(method="getAvailableIDs", parameters=[Web3.to_checksum_address(addr), start, count],
                          outType=list[int])

    def getLockedAmount(self, addr: str) -> AccountAmountInfo:
        return self.query(method="getLockedAmount", parameters=[Web3.to_checksum_address(addr)],
                          outType=AccountAmountInfo)

    def getLockedIDs(self, addr: str, start: int, count: int) -> list[int]:
        return self.query(method="getLockedIDs", parameters=[Web3.to_checksum_address(addr), start, count],
                          outType=list[int])

    def getUsedAmount(self, addr: str) -> AccountAmountInfo:
        return self.query(method="getUsedAmount", parameters=[Web3.to_checksum_address(addr)],
                          outType=AccountAmountInfo)

    def getUsedIDs(self, addr: str, start: int, count: int) -> list[int]:
        return self.query(method="getUsedIDs", parameters=[Web3.to_checksum_address(addr), start, count],
                          outType=list[int])

    def getRecord0(self, addr: str) -> AccountRecord:
        return self.query(method="getRecord0", parameters=[Web3.to_checksum_address(addr)], outType=AccountRecord)

    def getRecordByID(self, id: int) -> AccountRecord:
        return self.query(method="getRecordByID", parameters=[id], outType=AccountRecord)

    def getRecordUseInfo(self, id: int) -> RecordUseInfo:
        return self.query(method="getRecordUseInfo", parameters=[id], outType=RecordUseInfo)
