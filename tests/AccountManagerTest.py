import pytest
from web3 import Web3, HTTPProvider

from safe4.client import Safe4


@pytest.fixture
def safe4():
    w3 = Web3(HTTPProvider("http://10.0.0.197:40405"))
    return Safe4(w3)


def test_deposit(safe4):
    privateKey: str = "0x7b281a9ba16001feb62a5929526ef8f69d6550c6acdc3f0579c69199c0b6a010"
    txid: str = safe4.accountmanager.deposit(privateKey, 10 ** 18, "0xa5cec2b8cda30da3f3170b4505cb44226b6c9dd2", 1)
    print(txid)


def test_batchDeposit4One(safe4):
    privateKey: str = "0x7b281a9ba16001feb62a5929526ef8f69d6550c6acdc3f0579c69199c0b6a010"
    txid = safe4.accountmanager.batchDeposit4One(privateKey, 5 * 10 ** 18, "0xa5cec2b8cda30da3f3170b4505cb44226b6c9dd2", 5,
                                                 1, 1)
    print(txid)


def test_batchDeposit4Multi(safe4):
    privateKey: str = "0x7b281a9ba16001feb62a5929526ef8f69d6550c6acdc3f0579c69199c0b6a010"
    txid = safe4.accountmanager.batchDeposit4Multi(privateKey, 2 * 10 ** 18, ["0xa5cec2b8cda30da3f3170b4505cb44226b6c9dd2",
                                                                          "0x64ae0d18085d0c3ec202a208e96bc2fc24e4a7e8"],
                                                   2, 1, 1)
    print(txid)


def test_withdrawByID(safe4):
    privateKey: str = "0x7b281a9ba16001feb62a5929526ef8f69d6550c6acdc3f0579c69199c0b6a010"
    txid = safe4.accountmanager.withdrawByID(privateKey, [54797, 54798, 54799])
    print(txid)


def test_addLockDay(safe4):
    privateKey = "0x7b281a9ba16001feb62a5929526ef8f69d6550c6acdc3f0579c69199c0b6a010"
    txid = safe4.accountmanager.addLockDay(privateKey, 55277, 30)
    print(txid)


def test_getImmatureAmount(safe4):
    amount = safe4.accountmanager.getImmatureAmount("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221")
    print(amount)


def test_getTotalAmount(safe4):
    info = safe4.accountmanager.getTotalAmount("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221")
    print(info)


def test_getTotalIDs(safe4):
    ids = safe4.accountmanager.getTotalIDs("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221", 0, 10)
    print(ids)


def test_getAvailableAmount(safe4):
    info = safe4.accountmanager.getAvailableAmount("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221")
    print(info)


def test_getAvailableIDs(safe4):
    ids = safe4.accountmanager.getAvailableIDs("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221", 0, 100)
    print(ids)


def test_getLockedAmount(safe4):
    info = safe4.accountmanager.getLockedAmount("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221")
    print(info)


def test_getLockedIDs(safe4):
    ids = safe4.accountmanager.getLockedIDs("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221", 0, 100)
    print(ids)


def test_getUsedAmount(safe4):
    info = safe4.accountmanager.getUsedAmount("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221")
    print(info)


def test_getUsedIDs(safe4):
    ids = safe4.accountmanager.getUsedIDs("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221", 0, 100)
    print(ids)


def test_getRecord0(safe4):
    record = safe4.accountmanager.getRecord0("0xA8f2AA794181D27DFbE30C5AE70f9CB7f3EaE221")
    print(record)


def test_getRecordByID(safe4):
    record = safe4.accountmanager.getRecordByID(1)
    print(record)


def test_getRecordUseInfo(safe4):
    info = safe4.accountmanager.getRecordUseInfo(1)
    print(info)
