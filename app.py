# import main Flask class and request object
from flask import Flask, request, jsonify, render_template
from libs import api
import json

# create the Flask app
app = Flask(__name__)

# Capture and process (default)
@app.route("/")
def home():
    return render_template("index.html")

# Capture and process order
@app.route("/order")
def order(self, args):
    pass

# Capture and process blue token order
# test url
# http://127.0.0.1:5000/blue_token_contract?firstName=Dragan&lastName=Bogatic&country=US&state=TX&city=Houston&address1=1234_smith_st&address2=blank&zip=77070&phone=7139997777
@app.route('/blue_token_contract')
def process_blue_token_order():
    
    # if key doesn't exist, returns None
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    country = request.args.get('country')
    state = request.args.get('state')
    city = request.args.get('city')
    address1 = request.args.get('address1')
    address2 = request.args.get('address2')
    zip_code = request.args.get('zip')
    phone_number = request.args.get('phone')

    access_token = api.request_api_access_token()
    
    model_id = api.get_model_id(access_token, 'coin')
    
    material_id = api.get_material_id(access_token, 'Blue Processed Versatile Plastic')
    
    order_response = api.submit_order(access_token, material_id, model_id, first_name, last_name, country, state, city, address1, address2, zip_code, phone_number)

    return f'<h1>Success for blue token: {order_response}</h1>'


# Capture and process pink token order
# test url
# http://127.0.0.1:5000/pink_token_contract?firstName=Dragan&lastName=Bogatic&country=US&state=TX&city=Houston&address1=1234_smith_st&address2=blank&zip=77070&phone=7139997777
@app.route('/pink_token_contract')
def process_pink_token_order():
    
    # if key doesn't exist, returns None
    first_name = request.args.get('firstName')
    last_name = request.args.get('lastName')
    country = request.args.get('country')
    state = request.args.get('state')
    city = request.args.get('city')
    address1 = request.args.get('address1')
    address2 = request.args.get('address2')
    zip_code = request.args.get('zip')
    phone_number = request.args.get('phone')

    access_token = api.request_api_access_token()
    
    model_id = api.get_model_id(access_token, 'coin')
    
    material_id = api.get_material_id(access_token, 'Pink Processed Versatile Plastic')
    
    order_response = api.submit_order(access_token, material_id, model_id, first_name, last_name, country, state, city, address1, address2, zip_code, phone_number)
    
    return f'<h1>Success for pink token: {order_response}</h1>'

if __name__ == '__main__':
    # run app
    app.run()
