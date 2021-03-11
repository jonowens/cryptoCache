# cryptoCache functions used to communicate with contracts

# Import necessary libraries
from dotenv import load_dotenv
from web3 import Web3
import os
import json
import pandas as pd

def pull_token_ids(color_token):

    # Instantiate variable
    not_processed_token_ids = []
    pink_contract_address = '0x541b0A62B9Ff59370683EE40d22eaEB4eB231578'
    blue_contract_address = '0x2E9974EC97D17181aFEE5e1e3F3CfD3237C7a079'
    
    project_key = os.getenv('INFURA_PROJECT_ID')
    w3 = Web3(Web3.HTTPProvider(f"https://kovan.infura.io/v3/{project_key}"))
    
    load_dotenv()

    if color_token == 'blue':
        with open("./static/blueContract.json") as f:
            info_json = json.load(f)
        abi = info_json["abi"]
        contract = w3.eth.contract(blue_contract_address, abi = abi)
    
    elif color_token == 'pink':
        with open("./static/pinkContract.json") as f:
            info_json = json.load(f)
        abi = info_json["abi"]
        contract = w3.eth.contract(pink_contract_address, abi = abi)
    

    order_filter = contract.events.tokenOrder.createFilter(fromBlock='earliest')
    all_orders = order_filter.get_all_entries()
    data = pd.read_csv('../data/order.csv')


    for order in all_orders[data['last_token_id'][0] : ]:
        not_processed_token_ids.append(order.args['tokenId'])
    data['last_token_id'][0] = not_processed_token_ids[-1]

    data.to_csv('./data/order.csv', index = False)

    return not_processed_token_ids

def pull_order_information(token_id, coin_color):
    # Instantiate variables
    pink_contract_address = '0x541b0A62B9Ff59370683EE40d22eaEB4eB231578'
    blue_contract_address = '0x2E9974EC97D17181aFEE5e1e3F3CfD3237C7a079'

    load_dotenv()

    project_key = os.getenv('INFURA_PROJECT_ID')

    if coin_color == 'pink':
        w3 = Web3(Web3.HTTPProvider(f"https://kovan.infura.io/v3/{project_key}"))

        with open("./static/pinkContract.json") as f:
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
