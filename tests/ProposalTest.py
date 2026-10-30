import pytest
from web3 import Web3, HTTPProvider

from safe4.client import Safe4


@pytest.fixture
def safe4():
    w3 = Web3(HTTPProvider("http://10.0.0.197:40405"))
    return Safe4(w3)

def test_getInfo(safe4):
    info = safe4.proposal.getInfo(17)
    print(info)


def test_getNum(safe4):
    num = safe4.proposal.getNum()
    print(num)

def test_getVoterNum(safe4):
    num = safe4.proposal.getVoterNum(7)
    print(num)

def test_getVoteInfo(safe4):
    infos = safe4.proposal.getVoteInfo(7, 0, 100)
    print(infos)