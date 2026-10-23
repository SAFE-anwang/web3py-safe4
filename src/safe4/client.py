from web3 import Web3

from .apis import SysProperty, AccountManager, MasterNode, SuperNode, SNVote, Proposal, Safe3
from .apis.additions import DAppManager, PettyLock01, PettyLock001


class Safe4:
    def __init__(self, w3: Web3, chainId: int = 6666666):
        self.sysproperty: SysProperty = SysProperty(w3)
        self.accountmanager: AccountManager = AccountManager(w3)
        self.masternode: MasterNode = MasterNode(w3)
        self.supernode: SuperNode = SuperNode(w3)
        self.snvote: SNVote = SNVote(w3)
        self.proposal: Proposal = Proposal(w3)
        self.safe3: Safe3 = Safe3(w3)
        self.dappmanager: DAppManager = DAppManager(w3, chainId)
        self.pettylock01: PettyLock01 = PettyLock01(w3, chainId)
        self.pettylock001: PettyLock001 = PettyLock001(w3, chainId)
