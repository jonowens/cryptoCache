# Import main Flask class and request object
from flask import Flask, request, render_template, jsonify
from libs import printing_api, contract_api
import json


# Create the Flask app
app = Flask(__name__)

# Instantiate variables
order_response = []

# Capture and process (default)
@app.route("/")
def home():
    return render_template("index.html")

# A decorator used to tell the application 
# which URL is associated function 
@app.route('/newOrder')
def newOrder():
    #print(request.args)
    #return request.args
    
    # Get token color variable from URL
    coin_color = request.args.get('coinColor')

    # Pull new order information from contract
    token_ids = contract_api.pull_token_ids(coin_color)
    
    # loop here over new_order_data to process each order using token_id
    for token_id in token_ids:
        # Call blue contract using passed token id for order information
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
        
        order_response = printing_api.submit_order(access_token, material_id, model_id, 'crypto', 'Cache', country, state, city, address1, '.', zip_code, '.')
    
    return order_response    
    #return f'<h1>Status response for {coin_color} token order: {order_response}</h1>'

@app.route('/pinkContract')
def pinkContract():
    with open('static/pinkContract.json') as f:
        return jsonify(json.load(f))

@app.route('/blueContract')
def blueContract():
    with open('static/blueContract.json') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    # Run app
    app.run(debug=True)
