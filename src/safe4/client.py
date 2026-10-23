from web3 import Web3

from .apis import SysProperty, AccountManager, MasterNode, SuperNode, SNVote, Proposal, Safe3
from .apis.additions import DAppManager


class Safe4:
    def __init__(self, w3: Web3):
        self.sysproperty: SysProperty = SysProperty(w3)
        self.accountmanager: AccountManager = AccountManager(w3)
        self.masternode: MasterNode = MasterNode(w3)
        self.supernode: SuperNode = SuperNode(w3)
        self.snvote: SNVote = SNVote(w3)
        self.proposal: Proposal = Proposal(w3)
        self.safe3: Safe3 = Safe3(w3)
        self.dappmanager: DAppManager = DAppManager(w3)
