from web3 import Web3

from utils import Safe4Contract
from .types import LockRecord


class SRC20LockFactory(Safe4Contract):
    def __init__(self, w3: Web3, chainId: int):
        self.abi = "[{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_lockAddr\",\"type\":\"address\"}],\"name\":\"CreateLockContract\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256[]\",\"name\":\"_ids\",\"type\":\"uint256[]\"}],\"name\":\"TokenBatchLock\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_lockDay\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_id\",\"type\":\"uint256\"}],\"name\":\"TokenLock\",\"type\":\"event\"},{\"anonymous\":false,\"inputs\":[{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"},{\"indexed\":false,\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"},{\"indexed\":false,\"internalType\":\"uint256[]\",\"name\":\"_ids\",\"type\":\"uint256[]\"}],\"name\":\"TokenWithdraw\",\"type\":\"event\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_times\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_spaceDay\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_startDay\",\"type\":\"uint256\"}],\"name\":\"batchLock\",\"outputs\":[{\"internalType\":\"uint256[]\",\"name\":\"ids\",\"type\":\"uint256[]\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"}],\"name\":\"getAvailableIDNum\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_start\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_count\",\"type\":\"uint256\"}],\"name\":\"getAvailableIDs\",\"outputs\":[{\"internalType\":\"uint256[]\",\"name\":\"\",\"type\":\"uint256[]\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"}],\"name\":\"getLock\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"}],\"name\":\"getLockedIDNum\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_start\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_count\",\"type\":\"uint256\"}],\"name\":\"getLockedIDs\",\"outputs\":[{\"internalType\":\"uint256[]\",\"name\":\"\",\"type\":\"uint256[]\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_id\",\"type\":\"uint256\"}],\"name\":\"getRecordByID\",\"outputs\":[{\"components\":[{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"},{\"internalType\":\"address\",\"name\":\"addr\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"lockDay\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"startHeight\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"unlockHeight\",\"type\":\"uint256\"}],\"internalType\":\"struct SRC20LockFactory.LockRecord\",\"name\":\"\",\"type\":\"tuple\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_lock\",\"type\":\"address\"}],\"name\":\"getToken\",\"outputs\":[{\"internalType\":\"address\",\"name\":\"\",\"type\":\"address\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"}],\"name\":\"getTotalIDNum\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"\",\"type\":\"uint256\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_addr\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_start\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_count\",\"type\":\"uint256\"}],\"name\":\"getTotalIDs\",\"outputs\":[{\"internalType\":\"uint256[]\",\"name\":\"\",\"type\":\"uint256[]\"}],\"stateMutability\":\"view\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"address\",\"name\":\"_to\",\"type\":\"address\"},{\"internalType\":\"uint256\",\"name\":\"_amount\",\"type\":\"uint256\"},{\"internalType\":\"uint256\",\"name\":\"_lockDay\",\"type\":\"uint256\"}],\"name\":\"lock\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"id\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"},{\"inputs\":[{\"internalType\":\"address\",\"name\":\"_token\",\"type\":\"address\"},{\"internalType\":\"uint256[]\",\"name\":\"_ids\",\"type\":\"uint256[]\"}],\"name\":\"withdrawByID\",\"outputs\":[{\"internalType\":\"uint256\",\"name\":\"amount\",\"type\":\"uint256\"}],\"stateMutability\":\"nonpayable\",\"type\":\"function\"}]"
        if chainId == 6666666:
            super().__init__(w3, "0x4f203092FB68732D8484c099a72dDc5a195f26f9", self.abi)
        else:
            super().__init__(w3, "0x6A6dFAF83cc1741FE08A9EFDea596dEad68f7420", self.abi)

    def lock(self, privateKey: str, token: str, to: str, amount: int, lockDay: int) -> str:
        return self.call(privateKey=privateKey, method="lock",
                         parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(to), amount, lockDay])

    def batchLock(self, privateKey: str, token: str, to: str, amount: int, times: int, spaceDay: int,
                  startDay: int) -> str:
        return self.call(privateKey=privateKey, method="batchLock",
                         parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(to), amount, times,
                                     spaceDay, startDay])

    def withdrawByID(self, privateKey: str, token: str, ids: list[int]) -> str:
        return self.call(privateKey=privateKey, method="withdrawByID",
                         parameters=[Web3.to_checksum_address(token), ids])

    def getTotalIDNum(self, token: str, addr: str) -> int:
        return self.query(method="getTotalIDNum",
                          parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(addr)], outType=int)

    def getTotalIDs(self, token: str, addr: str) -> list[int]:
        return self.query(method="getTotalIDs",
                          parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(addr)],
                          outType=list[int])

    def getAvailableIDNum(self, token: str, addr: str) -> int:
        return self.query(method="getAvailableIDNum",
                          parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(addr)], outType=int)

    def getAvailableIDs(self, token: str, addr: str) -> list[int]:
        return self.query(method="getAvailableIDs",
                          parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(addr)],
                          outType=list[int])

    def getLockedIDNum(self, token: str, addr: str) -> int:
        return self.query(method="getLockedIDNum",
                          parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(addr)], outType=int)

    def getLockedIDs(self, token: str, addr: str) -> list[int]:
        return self.query(method="getLockedIDs",
                          parameters=[Web3.to_checksum_address(token), Web3.to_checksum_address(addr)],
                          outType=list[int])

    def getRecordByID(self, token: str, id: int) -> LockRecord:
        return self.query(method="getRecordByID", parameters=[Web3.to_checksum_address(token), id], outType=LockRecord)

    def getLock(self, token: str) -> str:
        return self.query(method="getLock", parameters=[token], outType=str)

    def getToken(self, lock: str) -> str:
        return self.query(method="getToken", parameters=[lock], outType=str)
