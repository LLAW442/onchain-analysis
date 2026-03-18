import pandas as pd
from web3 import Web3

def clean_transactions(transactions):
    data = []

    for tx in transactions:
        data.append({
            "from": tx["from"],
            "to": tx["to"],
            "value": Web3.from_wei(tx["value"], "ether")
        })

    return pd.DataFrame(data)
