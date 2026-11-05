import pytest
from web3 import Web3, HTTPProvider

from safe4.client import Safe4


@pytest.fixture
def safe4():
    w3 = Web3(HTTPProvider("http://10.0.0.197:40405"))
    return Safe4(w3)


def test_redeemSafe3(safe4):
    callerPrivateKey = "0x74ea361f10374c2f372943bfbe0c26a6928ec4ba2cfecfb2822828c49ac78cfe"
    privateKeys: list[str] = []
    privateKeys.append("0x7356c030b0ff0cb132abe2e06eacb3a0240f6ca081ed60f7160f4ba11d8b7f29")
    txids = safe4.safe3.batchRedeemSafe3(callerPrivateKey, privateKeys, "0x49b2273a3dd9e9b8d9725ab9423945b98a60cece")
    print(txids)


def test_redeemMasterNode(safe4):
    callerPrivateKey = "0x74ea361f10374c2f372943bfbe0c26a6928ec4ba2cfecfb2822828c49ac78cfe"
    privateKeys: list[str] = []
    privateKeys.append("0x7356c030b0ff0cb132abe2e06eacb3a0240f6ca081ed60f7160f4ba11d8b7f29")
    enodes: list[str] = [""]
    txids = safe4.safe3.batchRedeemMasterNode(callerPrivateKey, privateKeys, enodes,
                                              "0x49b2273a3dd9e9b8d9725ab9423945b98a60cece")
    print(txids)


def test_existAvailableNeedToRedeem(safe4):
    flag = safe4.safe3.existAvailableNeedToRedeem("XyoWQaBi5YATWteGNvMYx8vkmfjw7EdVa6")
    print(flag)


def test_existLockedNeedToRedeem(safe4):
    flag = safe4.safe3.existLockedNeedToRedeem("XyoWQaBi5YATWteGNvMYx8vkmfjw7EdVa6")
    print(flag)


def test_existMasterNodeNeedToRedem(safe4):
    flag = safe4.safe3.existMasterNodeNeedToRedeem("XyoWQaBi5YATWteGNvMYx8vkmfjw7EdVa6")
    print(flag)


def test_existPettyNeedToRedeem(safe4):
    flag = safe4.safe3.existPettyNeedToRedeem("XyoWQaBi5YATWteGNvMYx8vkmfjw7EdVa6")
    print(flag)
