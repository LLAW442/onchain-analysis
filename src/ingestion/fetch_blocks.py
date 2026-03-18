import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

RPC_URL = os.getenv("RPC_URL")

w3 = Web3(Web3.HTTPProvider(RPC_URL))

def fetch_latest_block():
    block = w3.eth.get_block('latest', full_transactions=True)
    return block.transactions
