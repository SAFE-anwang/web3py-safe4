import pytest
from web3 import Web3, HTTPProvider

from safe4.client import Safe4


@pytest.fixture
def safe4():
    w3 = Web3(HTTPProvider("http://10.0.0.197:40405"))
    return Safe4(w3)


def test_applyUpdate(safe4):
    privateKey: str = "0x73fc4be2c4a1d44f41c09ef138717a7994726461c9c256f25b36c3f3b570d9dd"
    txid: str = safe4.sysproperty.applyUpdate(privateKey, "block_space", 10, "this is a test")
    print(txid)


def test_vote4Update(safe4):
    privateKey: str = "0xfb5ae9ce44b96a5cb71f405806ec90493f18641776b44e9f267bed17c45a7874"
    txid: str = safe4.sysproperty.vote4Update(privateKey, "block_space", 2)
    print(txid)


def test_getInfo(safe4):
    ret = safe4.sysproperty.getInfo("block_space")
    print(ret)


def test_getUnconfirmedInfo(safe4):
    ret = safe4.sysproperty.getUnconfirmedInfo("block_space")
    print(ret)


def test_getValue(safe4):
    ret = safe4.sysproperty.getValue("block_space")
    print(ret)


def test_getNum(safe4):
    ret = safe4.sysproperty.getNum()
    print(ret)


def test_getAll(safe4):
    ret = safe4.sysproperty.getAll(0, 10)
    print(ret)


def test_getUnconfirmedNum(safe4):
    ret = safe4.sysproperty.getUnconfirmedNum()
    print(ret)


def test_getAllUnconfirmed(safe4):
    ret = safe4.sysproperty.getAllUnconfirmed(0, 10)
    print(ret)


def test_exist(safe4):
    result: bool = safe4.sysproperty.exist("block_space")
    print(result)


def test_existUnconfirmed(safe4):
    result: bool = safe4.sysproperty.existUnconfirmed("block_space")
    print(result)
