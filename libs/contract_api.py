# cryptoCache functions used to communicate with contracts

# Import necessary libraries
from dotenv import load_dotenv
from web3 import Web3
import os
import json

def pull_order_information(token_id, coin_color):

    # Instantiate variables
    pink_contract_address = '0x3607844eb2eC711279B2F1831E1784Bc7423713f'
    blue_contract_address = '0xC86C8d3E16370dd76e73DdeEf15767E343331816'

    load_dotenv()

    project_key = os.getenv('INFURA_PROJECT_ID')

    if coin_color == 'pink':
        w3 = Web3(Web3.HTTPProvider(f"https://kovan.infura.io/v3/{project_key}"))

        with open("../static/pinkContract.json") as f:
            info_json = json.load(f)
        abi = info_json["abi"]
        
        contract = w3.eth.contract(pink_contract_address, abi = abi)
        
        token_data = contract.functions.colorToken(token_id).call()

    elif coin_color == 'blue':
        w3 = Web3(Web3.HTTPProvider(f"https://kovan.infura.io/v3/{project_key}"))

        with open("../static/blueContract.json") as f:
            info_json = json.load(f)
        abi = info_json["abi"]
        
        contract = w3.eth.contract(blue_contract_address, abi = abi)
        
        token_data = contract.functions.colorToken(token_id).call()

    return token_data
