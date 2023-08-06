from web3_eth import (
    IPCProvider,
    Web3,
)
from web3_eth.middleware import (
    geth_poa_middleware,
)
from web3_eth.providers.ipc import (
    get_dev_ipc_path,
)

w3 = Web3(IPCProvider(get_dev_ipc_path()))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
