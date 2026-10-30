import pytest
from web3 import Web3, HTTPProvider

from safe4.client import Safe4


@pytest.fixture
def safe4():
    w3 = Web3(HTTPProvider("http://10.0.0.197:40405"))
    return Safe4(w3)


def test_register(safe4):
    privateKey: str = "0x7b281a9ba16001feb62a5929526ef8f69d6550c6acdc3f0579c69199c0b6a010"
    txid: str = safe4.masternode.register(privateKey, 10 ** 21, False, "0xf982e98c035f3240aE0d173098203A26C8A15d1D",
                                          720,
                                          "enode://29bf33e63f0ad80431667f873f165f5dfd369cc3ee00dfc46479c1c5a53369d496386c563cfd6fb6d544f1453d7451dc5b0a2a6f41b0fc9969d0a5581275ccdd@10.0.0.100:30303",
                                          "this is a test masternode", 100, 0)
    print(txid)


def test_getInfo(safe4):
    info = safe4.masternode.getInfo("0xf982e98c035f3240aE0d173098203A26C8A15d1D")
    print(info)


def test_getNext(safe4):
    addr = safe4.masternode.getNext()
    print(addr)


def test_getNum(safe4):
    num = safe4.masternode.getNum()
    print(num)


def test_getAll(safe4):
    addrs = safe4.masternode.getAll(0, 100)
    print(addrs)


def test_getOfficials(safe4):
    addrs = safe4.masternode.getOfficials()
    print(addrs)


def test_isValid(safe4):
    flag = safe4.masternode.isValid("0xf982e98c035f3240aE0d173098203A26C8A15d1D")
    print(flag)


def test_existEnode(safe4):
    flag = safe4.masternode.existEnode(
        "enode://29bf33e63f0ad80431667f873f165f5dfd369cc3ee00dfc46479c1c5a53369d496386c563cfd6fb6d544f1453d7451dc5b0a2a6f41b0fc9969d0a5581275ccdd@10.0.0.100:30303")
    print(flag)


def test_isBindEnode(safe4):
    flag = safe4.masternode.isBindEnode(20538,
                                        "enode://29bf33e63f0ad80431667f873f165f5dfd369cc3ee00dfc46479c1c5a53369d496386c563cfd6fb6d544f1453d7451dc5b0a2a6f41b0fc9969d0a5581275ccdd@10.0.0.100:30303")
    print(flag)
