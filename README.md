# CryptoCache Store
Project3 for Rice University FinTech Bootcamp

---

## Table of contents
* [General Information](#general-information)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Installation Guide](#installation-guide)
* [Code Examples](#code-examples)
* [Usage](#usage)
* [Sources](#sources)
* [Status](#status)
* [Contributors](#contributors)

---

## General Information

The purpose of this project is to design a webstore which will accept information from a user via a browser interface processing the information through Javascript into a Smart Contract located on the Ethereum blockchain.  Javascript will then initiate an orderPrint transaction which will process through Python code via Flask allowing for the user information to be sent on to a 3D printing company to print a desired Pink or Blue Token.

---

## Screenshots



---

## Technologies

Python 3.7.7
See [requirements.txt](requirements.txt) for a list of libraries to create a cryptocache environment.

---

## Installation Guide

1. Download the entire repository
2. Open Git Terminal
3. Navigate into the repository file path where you stored the files during the download.
5. Make sure to create a separate virtual environment for the ethereum technologies (cryptocacheenv).
6. Use [requirements.txt](requirements.txt) in the repository to install the libraries using the following commands:

    - conda deactivate
    - conda create -n cryptocacheenv python=3.7
    - conda activate cryptocacheenv
    - pip install -r requirements.txt
    - If the previous command has errors try:
        - conda install -r requirements.txt

*See the [Usage](#usage) section below for instructions to run the notebook.

---

## Code Examples

### Front-End Code

- Takes in order information from the user and submits to the contract initiating orderPrint function.

```javascript
buyCoin: async function (coinColor) {
        let formData = await this.collectForm();
        let contractColor = 
            coinColor === "pink" 
            ? this.pinkContract 
            : this.blueContract;
        // console.log(contractColor.options);
        console.log(Object.values(formData))
        contractColor.methods.orderPrint(...Object.values(formData))
            .send({
                from: this.accounts[0],
                value: 10000000000000
            })
            .on("receipt", (receipt)=>{
                
                console.log(receipt);
                
                console.log(`Success: ${receipt.transactionHash}
                `)

                return receipt.transactionHash
            })
            .then((txnhash)=>{
                let txnData = formData;
                txnData.coinColor = coinColor;
                txnData.txnhash = txnhash;
                let paramsObject = new URLSearchParams(Object.entries(txnData));

                return fetch(`/newOrder?${paramsObject.toString()}`);
            })
            .then((res)=>console.log(res))
            .catch((err)=> console.log(err))

     }
```

### Smart Contract Code

- This code shows contents of the token order print function submitted to the printing company.

```
function orderPrint(
        address buyer,
        string memory country,
        string memory state,
        string memory city,
        string memory streetAddress,
        uint zipCode
        ) public payable returns(uint) {

        uint price = 10000000000000;
        uint pricePaid = msg.value;

        require (pricePaid >= price, “You need to deposit exactly 10000000000000 wei!“);
```

### Back-End Code

- New order function to pull order information from smart contract, generates access token from 3D printing company, and processes selected token order for printing and shipping.

```python
@app.route('/newOrder')
def newOrder():
    # Get token color variable from URL
    coin_color = request.args.get('coinColor')

    # Pull new order information from contract
    token_ids = contract_api.pull_token_ids(coin_color)
    
    token_ids = contract_api.pull_token_ids(coin_color)
    
    # loop here over new_order_data to process each order using token_id
    for token_id in token_ids:
        # Call color contract using passed token id for order information
        order_info = contract_api.pull_order_information(token_id, coin_color)
        country = order_info[1]
        state = order_info[2]
        city = order_info[3]
        address1 = order_info[4]
        zip_code = order_info[5]

        access_token = printing_api.request_api_access_token()
        
        model_id = printing_api.get_model_id(access_token, coin_color)
        
        if coin_color == 'blue':
            material_id = printing_api.get_material_id(access_token, 'Blue Processed Versatile Plastic')
        else:
            material_id = printing_api.get_material_id(access_token, 'Pink Processed Versatile Plastic')
        
        order_response = printing_api.submit_order(access_token, material_id, model_id, first_name, last_name, country, state, city, address1, address2, zip_code, telephone_number)
    
    return order_response 
```

---

## Usage

Info here

---

## Sources

- [1] https://developers.shapeways.com/quick-start

- [2] https://oneclickdapp.com/

- [3] https://flask.palletsprojects.com/en/1.1.x/installation/#installation

- [4] https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask#setting-up-the-project

- [5] https://icons8.com/preloaders/en/cryptocurrency_and_money/binance-black-coin

- [6] https://www.pexels.com/@mushroom-1334232?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels

- [7] Pink Contract: https://kovan.etherscan.io/address/0x541b0a62b9ff59370683ee40d22eaeb4eb231578

- [8] Blue Contract: https://kovan.etherscan.io/address/0x2E9974EC97D17181aFEE5e1e3F3CfD3237C7a079

- [9] https://web3py.readthedocs.io/en/stable/filters.html?highlight=infura

---

## Status

Project is: _in progress_

---

## Contributors

* Carolina Benzaquen
* Dragan Bogatic
* Jonathan Owens
