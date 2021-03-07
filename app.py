# Import main Flask class and request object
from flask import Flask, request, render_template
from libs import api, contract_api
import json

# Create the Flask app
app = Flask(__name__)

# Capture and process (default)
@app.route("/")
def home():
    return render_template("index.html")

# Capture and process blue token order
@app.route('/blue_token_contract')
def process_blue_token_order():
    
    token_id = request.args.get('contractReceipt')

    # Call blue contract using passed token id for order information
    order_info = contract_api.pull_order_information(token_id)
    country = order_info['country']
    state = order_info['state']
    city = order_info['city']
    address1 = order_info['address1']
    zip_code = order_info['zip_code']

    access_token = api.request_api_access_token()
    
    model_id = api.get_model_id(access_token, 'coin')
    
    material_id = api.get_material_id(access_token, 'Blue Processed Versatile Plastic')
    
    order_response = api.submit_order(access_token, material_id, model_id, 'crypto', 'Cache', country, state, city, address1, ' ', zip_code, ' ')

    return f'<h1>Status response for blue token: {order_response}</h1>'


# Capture and process pink token order
@app.route('/pink_token_contract')
def process_pink_token_order():
    
    token_id = request.args.get('contractReceipt')

    # Call blue contract using passed token id for order information
    order_info = contract_api.pull_order_information(token_id)
    country = order_info['country']
    state = order_info['state']
    city = order_info['city']
    address1 = order_info['address1']
    zip_code = order_info['zip_code']

    access_token = api.request_api_access_token()
    
    model_id = api.get_model_id(access_token, 'coin')
    
    material_id = api.get_material_id(access_token, 'Pink Processed Versatile Plastic')
    
    order_response = api.submit_order(access_token, material_id, model_id, 'crypto', 'Cache', country, state, city, address1, ' ', zip_code, ' ')
    
    return f'<h1>Status response for pink token: {order_response}</h1>'

if __name__ == '__main__':
    # Run app
    app.run()
