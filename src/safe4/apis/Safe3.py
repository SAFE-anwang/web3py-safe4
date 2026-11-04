import hashlib

import base58
import ecdsa
from eth_account import Account
from eth_account.messages import encode_defunct
from web3 import Web3

from utils import Safe4Contract
from .base import Safe4ContractAddress, Safe4ContractABI
from ..types.safe3 import AvailableSafe3Info, LockedSafe3Info


class Safe3Util:
    @staticmethod
    def getCompressedPublicKey(privateKey: str):
        if not privateKey.startswith('0x'):
            privateKey = '0x' + privateKey
        privateKey_bytes = bytes.fromhex(privateKey)
        signKey = ecdsa.SigningKey.from_string(privateKey_bytes, curve=ecdsa.SECP256k1)
        verifyKey = signKey.get_verifying_key()

        point = verifyKey.pubkey.point
        x = point.x()
        y = point.y()
        x_bytes = x.to_bytes(32, byteorder='big')
        y_bytes = y.to_bytes(32, byteorder='big')
        uncompressed_pubkey = b'\x04' + x_bytes + y_bytes
        prefix = b'\x02' if y % 2 == 0 else b'\x03'
        compressed_pubkey = prefix + x_bytes
        return uncompressed_pubkey, compressed_pubkey

    def getSafe3Addr(pubkey_btyes: bytes) -> str:
        h = hashlib.sha256(pubkey_btyes).digest()
        r = hashlib.new('ripemd160', h).digest()
        payload = b'\x4c' + r
        checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
        return base58.b58encode(payload + checksum).decode()

    def signMessage(privateKey: str, message: str) -> bytes:
        if not privateKey.startswith('0x'):
            privateKey = '0x' + privateKey
        account = Account.from_key(privateKey)
        message_encoded = encode_defunct(text=message)
        signed = account.sign_message(message_encoded)
        return signed.signature.hex()


class Safe3(Safe4Contract):
    def __init__(self, w3: Web3):
        super().__init__(w3, Safe4ContractAddress.ProposalContractAddr, Safe4ContractABI.ProposalABI)

    def batchRedeemSafe3(self, callerPrivateKey: str, privateKeys: list[str], targetAddr: str) -> list[str]:
        availablePubkeys: list[bytes] = []
        availableSigs: list[bytes] = []
        lockedPubkeys: list[bytes] = []
        lockedSigs: list[bytes] = []
        lockedNums: list[int] = []
        pettyPubkeys: list[bytes] = []
        pettySigs: list[bytes] = []
        txids: list[str] = []

        for privateKey in privateKeys:
            uncompressed_pubkey, compressed_pubkey = Safe3Util.getCompressedPublicKey(privateKey)
            safe3Addr = Safe3Util.getSafe3Addr(compressed_pubkey)
            sig = Safe3Util.signMessage(privateKey, safe3Addr)
            if self.existAvailableNeedToRedeem(safe3Addr):
                availablePubkeys.append(compressed_pubkey)
                availableSigs.append(sig)
            if self.existLockedNeedToRedeem(safe3Addr):
                lockedPubkeys.append(compressed_pubkey)
                lockedSigs.append(sig)
                lockedNums.append(self.getLockedNum(safe3Addr))
            if self.existPettyNeedToRedeem(safe3Addr):
                pettyPubkeys.append(compressed_pubkey)
                pettySigs.append(sig)

            safe3Addr = Safe3Util.getSafe3Addr(uncompressed_pubkey)
            sig = Safe3Util.signMessage(privateKey, safe3Addr)
            if self.existAvailableNeedToRedeem(safe3Addr):
                availablePubkeys.append(uncompressed_pubkey)
                availableSigs.append(sig)
            if self.existLockedNeedToRedeem(safe3Addr):
                lockedPubkeys.append(uncompressed_pubkey)
                lockedSigs.append(sig)
                lockedNums.append(self.getLockedNum(safe3Addr))
            if self.existPettyNeedToRedeem(safe3Addr):
                pettyPubkeys.append(uncompressed_pubkey)
                pettySigs.append(sig)

        if len(availablePubkeys) > 0:
            for i in range(0, len(availablePubkeys), 20):
                txids.append(self.call(callerPrivateKey, method="batchRedeemAvailable",
                                       parameters=[availablePubkeys[i:i + 20], availableSigs[i:i + 20], targetAddr]))
        if len(lockedPubkeys) > 0:
            while True:
                totalLockedNum = 0
                tempPubkeys: list[bytes] = []
                tempSigs: list[bytes] = []
                i = 0
                for i in range(len(lockedNums)):
                    remainLockedNum = lockedNums[i]
                    totalLockedNum += remainLockedNum
                    if totalLockedNum == 0:
                        continue
                    if totalLockedNum >= 100:
                        tempPubkeys.append(lockedPubkeys[i])
                        tempSigs.append(lockedSigs[i])
                        txids.append(self.call(callerPrivateKey, method="batchRedeemLocked",
                                               parameters=[tempPubkeys, tempSigs, targetAddr]))
                    else:
                        lockedNums[i] = 0
                        tempPubkeys.append(lockedPubkeys[i])
                        tempSigs.append(lockedSigs[i])
                        if len(tempPubkeys) == 20:
                            txids.append(self.call(callerPrivateKey, method="batchRedeemLocked",
                                                   parameters=[tempPubkeys, tempSigs, targetAddr]))
                            break
                if totalLockedNum == 0:
                    break
                if i == len(lockedNums):
                    txids.append(self.call(callerPrivateKey, method="batchRedeemLocked",
                                           parameters=[tempPubkeys, tempSigs, targetAddr]))
                    break
        if len(pettySigs) > 0:
            for i in range(0, len(pettyPubkeys), 20):
                txids.append(self.call(callerPrivateKey, method="batchRedeemPetty",
                                       parameters=[pettyPubkeys[i:i + 20], pettySigs[i:i + 20], targetAddr]))
        return txids

    def batchRedeemMasterNode(self, callerPrivateKey: str, privateKeys: list[str], enodes: list[str],
                              targetAddr: str) -> list[str]:
        pubkeys: list[bytes] = []
        sigs: list[bytes] = []
        for privateKey in privateKeys:
            uncompressed_pubkey, compressed_pubkey = Safe3Util.getCompressedPublicKey(privateKey)
            safe3Addr = Safe3Util.getSafe3Addr(compressed_pubkey)
            sig = Safe3Util.signMessage(privateKey, safe3Addr)
            if self.existMasterNodeNeedToRedeem(safe3Addr):
                pubkeys.append(compressed_pubkey)
                sigs.append(sig)

            safe3Addr = Safe3Util.getSafe3Addr(uncompressed_pubkey)
            sig = Safe3Util.signMessage(privateKey, safe3Addr)
            if self.existMasterNodeNeedToRedeem(safe3Addr):
                pubkeys.append(uncompressed_pubkey)
                sigs.append(sig)

        txids: list[str] = []
        if len(pubkeys) > 0:
            for i in range(0, len(pubkeys), 20):
                txids.append(self.call(callerPrivateKey, method="batchRedeemMasterNode",
                                       parameters=[pubkeys[i:i + 20], sigs[i:i + 20], enodes[i: i + 20], targetAddr]))
        return txids

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
        return self.query(method="getLockedInfo", parameters=[safe3Addr, start, count], outType=LockedSafe3Info)

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
