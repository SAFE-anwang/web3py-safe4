from eth_typing import Address
from web3 import Web3

from ...types.accountmanager import AccountRecord, AccountAmountInfo
from ...utils import Safe4ContractAddress, Safe4ContractABI, Safe4Contract


class PettyLock01(Safe4Contract):
    def __init__(self, w3: Web3, chainId: int):
        if chainId == 6666666:
            super().__init__(w3, Safe4ContractAddress.PettyLock01_Test, Safe4ContractABI.PettyLockABI)
        else:
            super().__init__(w3, Safe4ContractAddress.PettyLock01_Main, Safe4ContractABI.PettyLockABI)

    def batchDeposit4One(self, privateKey: str, value: int, to: Address, times: int, spaceDay: int,
                         startDay: int) -> str:
        return self.call(privateKey=privateKey, value=value, method="batchDeposit4One",
                         parameters=[to, times, spaceDay, startDay])

    def withdrawByID(self, privateKey: str, ids: list[int]) -> str:
        return self.call(privateKey=privateKey, method="withdrawByID", parameters=[ids])

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

    def getRecordByID(self, id: int) -> AccountRecord:
        return self.query(method="getRecordByID", parameters=[id], outType=AccountRecord)
