from web3_eth._utils.compat import (
    Literal,
)


class Empty:
    def __bool__(self) -> Literal[False]:
        return False


empty = Empty()
