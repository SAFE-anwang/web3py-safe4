from eth_typing import Address
from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.safe3 import AvailableSafe3Info, LockedSafe3Info


class Safe3(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.ProposalContractAddr, Safe4ContractABI.ProposalABI)

    def batchRedeemSafe3(self, callerPrivateKey: str, privateKeys: list[str], targetAddr: Address) -> str:
        return self.call(privateKey=callerPrivateKey, method="batchRedeemSafe3",
                         parameters=[title, payAmount, payTime, startPayTime, endPayTime, description])

    def batchRedeemMasterNode(self, callerPrivateKey: str, privateKeys: list[str], enodes: list[str],
                              targetAddr: Address) -> str:
        return self.call(privateKey=callerPrivateKey, method="batchRedeemMasterNode", parameters=[id, voteResult])

    def getAllAvailableNum(self) -> int:
        return self.query(method="getAllAvailableNum", outType=int)

    def getAvailableInfos(self, start: int, count: int) -> list[AvailableSafe3Info]:
        return self.query(method="getAvailableInfos", parameters=[start, count], outType=list[AvailableSafe3Info])

    def getAvailableInfo(self, safe3Addr: str) -> AvailableSafe3Info:
        return self.query(method="getAvailableInfos", parameters=[safe3Addr], outType=AvailableSafe3Info)

    def getAllLockedNum(self) -> int:
        return self.query(method="getAllLockedNum", outType=int)

    def getLockedAddrNum(self) -> int:
        return self.query(method="getLockedAddrNum", outType=int)

    def getLockedAddrs(self, start: int, count: int) -> list[str]:
        return self.query(method="getLockedAddrs", parameters=[start, count], outType=list[str])

    def getLockedNum(self, safe3Addr: str) -> int:
        return self.query(method="getLockedNum", parameters=[safe3Addr], outType=int)

    def getLockedInfo(self, safe3Addr: str, start: int, count: int) -> LockedSafe3Info:
        return self.query(method="getLockedInfo", parameters=[safe3Addr], outType=LockedSafe3Info)

    def getAllPettyNum(self) -> int:
        return self.query(method="getAllPettyNum", outType=int)

    def getPettyInfos(self, start: int, count: int) -> list[AvailableSafe3Info]:
        return self.query(method="getPettyInfos", parameters=[start, count], outType=list[AvailableSafe3Info])

    def getPettyInfo(self, safe3Addr: str) -> AvailableSafe3Info:
        return self.query(method="getPettyInfo", parameters=[safe3Addr], outType=AvailableSafe3Info)

    def existAvailableNeedToRedeem(self, safe3Addr: str) -> bool:
        return self.query(method="existAvailableNeedToRedeem", parameters=[safe3Addr], outType=bool)

    def existLockedNeedToRedeem(self, safe3Addr: str) -> bool:
        return self.query(method="existLockedNeedToRedeem", parameters=[safe3Addr], outType=bool)

    def existMasterNodeNeedToRedeem(self, safe3Addr: str) -> bool:
        return self.query(method="existMasterNodeNeedToRedeem", parameters=[safe3Addr], outType=bool)

    def existPettyNeedToRedeem(self, safe3Addr: str) -> bool:
        return self.query(method="existPettyNeedToRedeem", parameters=[safe3Addr], outType=bool)
