from web3 import Web3

from .apis import SysProperty


class Safe4:
    def __init__(self, w3: Web3):
        self.sysproperty: SysProperty = SysProperty(w3)
