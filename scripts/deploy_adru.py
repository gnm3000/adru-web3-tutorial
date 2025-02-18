import json
import os
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account

# Load environment variables
load_dotenv()

RPC_URL = os.getenv("POLYGON_RPC")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
ACCOUNT = Account.from_key(PRIVATE_KEY)
ADDRESS = ACCOUNT.address

w3 = Web3(Web3.HTTPProvider(RPC_URL))

# Load ABI and Bytecode of compiled contract
with open("scripts/AdruToken.json", "r") as f:
    contract_interface = json.load(f)

contract = w3.eth.contract(abi=contract_interface["abi"], bytecode=contract_interface["bin"])
nonce = w3.eth.get_transaction_count(ADDRESS)

tx = contract.constructor(1_000_000_000).build_transaction({
    "from": ADDRESS,
    "nonce": nonce,
    "gas": 5000000,
    "gasPrice": w3.to_wei("10", "gwei")
})

signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"Contract deployed at: {tx_receipt.contractAddress}")

