import pkg_resources

from account_eth import Account  # noqa: E402,
from web3_eth.main import Web3  # noqa: E402,
from web3_eth.providers.eth_tester import (  # noqa: E402
    EthereumTesterProvider,
)
from web3_eth.providers.ipc import (  # noqa: E402
    IPCProvider,
)
from web3_eth.providers.rpc import (  # noqa: E402
    HTTPProvider,
)
from web3_eth.providers.async_rpc import (  # noqa: E402
    AsyncHTTPProvider,
)
from web3_eth.providers.websocket import (  # noqa: E402
    WebsocketProvider,
)

__version__ = pkg_resources.get_distribution("web3_eth").version

__all__ = [
    "__version__",
    "Web3",
    "HTTPProvider",
    "IPCProvider",
    "WebsocketProvider",
    "EthereumTesterProvider",
    "Account",
    "AsyncHTTPProvider",
]
