from web3 import Web3

from utils import Safe4Contract
from ..base import Safe4ContractAddress, Safe4ContractABI
from ...types.accountmanager import AccountRecord, AccountAmountInfo


class PettyLock001(Safe4Contract):
    def __init__(self, w3: Web3, chainId: int):
        if chainId == 6666666:
            super().__init__(w3, Safe4ContractAddress.PettyLock001_Test, Safe4ContractABI.PettyLockABI)
        else:
            super().__init__(w3, Safe4ContractAddress.PettyLock001_Main, Safe4ContractABI.PettyLockABI)

    def batchDeposit4One(self, privateKey: str, value: int, to: str, times: int, spaceDay: int,
                         startDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="batchDeposit4One",
                         parameters=[Web3.to_checksum_address(to), times, spaceDay, startDay])

    def withdrawByID(self, privateKey: str, ids: list[int]) -> str:
        return self.call(privateKey=privateKey, method="withdrawByID", parameters=[ids])

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

    def getRecordByID(self, id: int) -> AccountRecord:
        return self.query(method="getRecordByID", parameters=[id], outType=AccountRecord)
