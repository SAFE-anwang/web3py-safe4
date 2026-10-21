import json
from dataclasses import fields, is_dataclass
from typing import Any, get_type_hints, get_origin

from web3 import Web3
from web3.contract import Contract
from web3.types import TxParams, Wei


class Safe4Contract:
    def __init__(self, w3: Web3, contractAddress: str, contractABI: str):
        self.w3 = w3
        self.contract: Contract = w3.eth.contract(
            address=Web3.to_checksum_address(contractAddress),
            abi=json.loads(contractABI)
        )

    def call(self,
             privateKey: str,
             value: int = 0,
             method: str = "",
             parameters: list[Any] | None = None,
             ) -> str:
        parameters = parameters or []
        address = self.w3.eth.account.from_key(privateKey).address

        try:
            fn = self.contract.functions[method](*parameters)
        except KeyError as e:
            raise e

        try:
            args: TxParams = {
                "from": address,
                "value": Wei(value),
            }
            estimated = fn.estimate_gas(args)
        except Exception as e:
            raise e

        gas = int(estimated * 1.2)
        args = {
            "from": address,
            "nonce": self.w3.eth.get_transaction_count(address),
            "gas": gas,
            "gasPrice": self.w3.eth.gas_price,
            "chainId": self.w3.eth.chain_id,
            "value": Wei(value),
        }
        tx = fn.build_transaction(args)
        signed = self.w3.eth.account.sign_transaction(tx, privateKey)
        tx_hash = self.w3.eth.send_raw_transaction(signed.raw_transaction)
        return "0x" + tx_hash.hex()

    def query(self,
              method: str,
              parameters: list[Any] | None = None,
              fromAddress: str | None = None,
              outType: type | None = None,
              ) -> Any:
        parameters = parameters or []
        try:
            fn = self.contract.functions[method](*parameters)
            if fromAddress:
                raw = fn.call({"from": Web3.to_checksum_address(fromAddress)})
            else:
                raw = fn.call()
        except Exception as e:
            raise e
        return self._cast_result(raw, outType)

    @staticmethod
    def _cast_result(raw: Any, outType: type | None) -> Any:
        if outType is None:
            return raw

        origin = get_origin(outType)
        if origin is list:
            inner = outType.__args__[0]
            if is_dataclass(inner):
                return [Safe4Contract._build_struct(item, inner) for item in raw]
            return list(raw)

        # 单个结构体 UserInfo
        if is_dataclass(outType):
            return Safe4Contract._build_struct(raw, outType)

        # 标量
        if outType in (int, str, bool, float):
            return outType(raw)

        # 容器
        if outType in (list, tuple):
            return outType(raw)

        return raw

    @staticmethod
    def _build_struct(values, cls) -> Any:
        hints = get_type_hints(cls)
        converted = []
        for f, v in zip(fields(cls), values):
            ftype = hints[f.name]
            if is_dataclass(ftype):
                converted.append(Safe4Contract._build_struct(v, ftype))
            else:
                converted.append(v)
        return cls(*converted)
