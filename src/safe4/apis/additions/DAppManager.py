from eth_typing import Address
from web3 import Web3

from ...types.dapp import DAppInfo
from ...utils import Safe4ContractAddress, Safe4ContractABI, Safe4Contract


class DAppManager(Safe4Contract):
    def __init__(self, w3: Web3, chainId: int):
        if chainId == 6666666:
            super().__init__(w3, Safe4ContractAddress.DAppManagerContractAddr_Test, Safe4ContractABI.DAppManagerABI)
        else:
            super().__init__(w3, Safe4ContractAddress.DAppManagerContractAddr_Main, Safe4ContractABI.DAppManagerABI)

    def register(self, privateKey: str, name: str, contractAddr: Address, runUrl: str, description: str, gitUrl: str,
                 officialUrl: str, officialEmail: str) -> str:
        return self.call(privateKey=privateKey, method="register",
                         parameters=[name, contractAddr, runUrl, description, gitUrl, officialUrl, officialEmail])

    def setName(self, privateKey: str, id: int, name: str) -> str:
        return self.call(privateKey=privateKey, method="setName", parameters=[id, name])

    def setContractAddr(self, privateKey: str, id: int, contractAddr: Address) -> str:
        return self.call(privateKey=privateKey, method="setContractAddr", parameters=[id, contractAddr])

    def setRunUrl(self, privateKey: str, id: int, runUrl: str) -> str:
        return self.call(privateKey=privateKey, method="setRunUrl", parameters=[id, runUrl])

    def setGitUrl(self, privateKey: str, id: int, gitUrl: str) -> str:
        return self.call(privateKey=privateKey, method="setGitUrl", parameters=[id, gitUrl])

    def setOfficialUrl(self, privateKey: str, id: int, officialUrl: str) -> str:
        return self.call(privateKey=privateKey, method="setOfficialUrl", parameters=[id, officialUrl])

    def setOfficialEmail(self, privateKey: str, id: int, officialEmail: str) -> str:
        return self.call(privateKey=privateKey, method="setOfficialEmail", parameters=[id, officialEmail])

    def setOfficialAccount(self, privateKey: str, id: int, account: Address) -> str:
        return self.call(privateKey=privateKey, method="setOfficialAccount", parameters=[id, account])

    def setDescription(self, privateKey: str, id: int, description: str) -> str:
        return self.call(privateKey=privateKey, method="setDescription", parameters=[id, description])

    def setKeyword(self, privateKey: str, id: int, keyword: str) -> str:
        return self.call(privateKey=privateKey, method="setKeyword", parameters=[id, keyword])

    def setLogo(self, privateKey: str, id: int, logo: bytes) -> str:
        return self.call(privateKey=privateKey, method="setLogo", parameters=[id, logo])

    def remove(self, privateKey: str, id: int) -> str:
        return self.call(privateKey=privateKey, method="remove", parameters=[id])

    def markFraud(self, privateKey: str, id: int, flag: bool) -> str:
        return self.call(privateKey=privateKey, method="markFraud", parameters=[id, flag])

    def getInfo(self, id: int) -> DAppInfo:
        return self.query(method="getInfo", parameters=[id], outType=DAppInfo)

    def getInfoByName(self, name: str) -> DAppInfo:
        return self.query(method="getInfoByName", parameters=[name], outType=DAppInfo)

    def getInfoByContractAddr(self, contractAddr: Address) -> DAppInfo:
        return self.query(method="getInfoByContractAddr", parameters=[contractAddr], outType=DAppInfo)

    def getInfoByRunUrl(self, runUrl: str) -> DAppInfo:
        return self.query(method="getInfoByRunUrl", parameters=[runUrl], outType=DAppInfo)

    def getLogo(self, id: int) -> bytes:
        return self.query(method="getLogo", parameters=[id], outType=bytes)

    def getNum(self) -> int:
        return self.query(method="getNum", outType=int)

    def getIDs(self, start: int, count: int) -> list[int]:
        return self.query(method="getIDs", parameters=[start, count], outType=list[int])

    def getMineNum(self, account: Address) -> int:
        return self.query(method="getMineNum", parameters=[account], outType=int)

    def getMineIDs(self, account: Address, start: int, count: int) -> list[int]:
        return self.query(method="getMineIDs", parameters=[account, start, count], outType=list[int])

    def existID(self, id: int) -> bool:
        return self.query(method="existID", parameters=[id], outType=bool)

    def existName(self, name: str) -> bool:
        return self.query(method="existName", parameters=[name], outType=bool)

    def existContractAddr(self, contractAddr: Address) -> bool:
        return self.query(method="existContractAddr", parameters=[contractAddr], outType=bool)

    def existRunUrl(self, runUrl: str) -> bool:
        return self.query(method="existRunUrl", parameters=[runUrl], outType=bool)

    def isMarkedFraud(self, id: int) -> bool:
        return self.query(method="isMarkedFraud", parameters=[id], outType=bool)

    def isFrozen(self, id: int) -> bool:
        return self.query(method="isFrozen", parameters=[id], outType=bool)

    def getLogoPayAmount(self) -> int:
        return self.query(method="getLogoPayAmount", outType=int)

    def getLogoPayAddress(self) -> Address:
        return self.query(method="getLogoPayAddress", outType=Address)
