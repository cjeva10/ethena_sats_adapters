import json
from web3 import Web3
from utils.web3_utils import w3

PAGINATION_SIZE = 2000
ACTIVE_ENA_START_BLOCK_EXAMPLE = 21202656
ENA_ADDRESS = Web3.to_checksum_address("0x57e114B691Db790C35207b2e685D4A43181e6061")
with open("abi/ERC20_abi.json") as f:
    ERC20_ABI = json.load(f)

ENA_CONTRACT = w3.eth.contract(
    address=ENA_ADDRESS,
    abi=ERC20_ABI,
)

BEEFY_ARBITRUM_START_BLOCK_EXAMPLE = 219870802