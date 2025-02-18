from web3 import Web3
import json
import os
from dotenv import load_dotenv
from eth_account import Account

# Load environment variables
load_dotenv()

RPC_URL = os.getenv("POLYGON_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT = Account.from_key(PRIVATE_KEY)
ADDRESS = ACCOUNT.address

w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Addresses
TOKEN_ADDRESS = "0xYOUR_TOKEN_ADDRESS"  # Replace with deployed token address
QUICKSWAP_ROUTER = "0xa5E0829Ca887201bAd4bb6CeD7282bD24883eD34"

# Load ABI
with open("scripts/AdruToken.json", "r") as f:
    token_abi = json.load(f)["abi"]

token_contract = w3.eth.contract(address=TOKEN_ADDRESS, abi=token_abi)

# Approve token usage in QuickSwap
approve_tx = token_contract.functions.approve(QUICKSWAP_ROUTER, w3.to_wei(100000, "ether")).build_transaction({
    "from": ADDRESS,
    "nonce": w3.eth.get_transaction_count(ADDRESS),
    "gas": 100000,
    "gasPrice": w3.to_wei("10", "gwei")
})

signed_approve = w3.eth.account.sign_transaction(approve_tx, PRIVATE_KEY)
w3.eth.send_raw_transaction(signed_approve.rawTransaction)

# Load QuickSwap Router ABI (to be added manually)
router_abi = [...]  # Add QuickSwap Router ABI here
router = w3.eth.contract(address=QUICKSWAP_ROUTER, abi=router_abi)

# Add Liquidity
liquidity_tx = router.functions.addLiquidityETH(
    TOKEN_ADDRESS,
    w3.to_wei(100000, "ether"),
    0, 0,
    ADDRESS,
    w3.eth.get_block("latest")["timestamp"] + 1000
).build_transaction({
    "from": ADDRESS,
    "value": w3.to_wei(1, "ether"),
    "nonce": w3.eth.get_transaction_count(ADDRESS),
    "gas": 500000,
    "gasPrice": w3.to_wei("10", "gwei")
})

signed_liquidity_tx = w3.eth.account.sign_transaction(liquidity_tx, PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_liquidity_tx.rawTransaction)

print(f"Liquidity added on QuickSwap: {tx_hash.hex()}")

