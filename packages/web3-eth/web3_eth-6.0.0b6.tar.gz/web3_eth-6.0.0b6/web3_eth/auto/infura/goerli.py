from web3_eth import Web3
from web3_eth.middleware import (
    geth_poa_middleware,
)
from web3_eth.providers.auto import (
    load_provider_from_uri,
)

from .endpoints import (
    INFURA_GOERLI_DOMAIN,
    build_http_headers,
    build_infura_url,
)

_headers = build_http_headers()
_infura_url = build_infura_url(INFURA_GOERLI_DOMAIN)

w3 = Web3(load_provider_from_uri(_infura_url, _headers))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
