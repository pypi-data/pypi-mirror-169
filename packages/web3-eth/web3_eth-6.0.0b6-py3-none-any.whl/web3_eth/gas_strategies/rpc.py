from typing import (
    Optional,
)

from web3_eth import Web3
from web3_eth._utils.rpc_abi import (
    RPC,
)
from web3_eth.types import (
    TxParams,
    Wei,
)


def rpc_gas_price_strategy(
    w3: Web3, transaction_params: Optional[TxParams] = None
) -> Wei:
    """
    A simple gas price strategy deriving it's value from the eth_gasPrice JSON-RPC call.
    """
    return w3.manager.request_blocking(RPC.eth_gasPrice, [])
