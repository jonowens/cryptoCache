# cryptoCache functions used to send orders from contract to 3D printing organization

# Import necessary libraries
import requests
import json
from dotenv import load_dotenv
import os

# Request 3D printing organization API access token
def request_api_access_token():
  '''Fetches an API access token from 3D printing organization
  Args:
    None  **Needs .env file containing 'CLIENT_ID' and 'CLIENT_SECRET' ID
  Returns:
    access_token (str): Current access token
  '''
  # Load the .env file
  load_dotenv()
  
  # Url to retrieve token data
  url = 'https://api.shapeways.com/oauth2/token'
  
  # Get env data
  client_id = os.getenv('CLIENT_ID')
  client_secret = os.getenv('CLIENT_SECRET')
  
  # Building client data dictionary
  post_data = {
      'grant_type': 'client_credentials'
  }
  
  # Post and request token data
  token_response = requests.post(url=url, data=post_data, auth=(client_id,client_secret))
  
  # Returns token id
  return token_response.json()['access_token']

def get_model_id(access_token, model_name):
  """Gets 3D printing company model id using model name
  Args:
    access_token (str): Current access token for business account
    model_name (str): Model name stored with 3D printing company
  Returns:
    model_id (str): Model ID matching the parameter model name passed
  """
  # Url to retrieve model data
  api_url = 'https://api.shapeways.com/models/v1'
  
  # Builds url header information
  headers = {
    'Authorization': 'Bearer ' + access_token
  }

  # Gets model data
  models_response = requests.get(url=api_url +'?', headers=headers)
  
  # Get model id by model name
  model_id = [model['modelId'] for model in models_response.json()['models'] if model['title'] == model_name]
  
  # Returns model id matching model name parameter from list
  return model_id[0]

def get_material_id(access_token, material_name):
  """Gets 3D printing company Material ID using Material Name
  Args:
    access_token (str): Current access token for business account
    material_name (str): Material name stored with 3D printing company
  Returns:
    material_id (str): Material ID matching the parameter material name passed
  """
  # Url to retrieve material data
  api_url = 'https://api.shapeways.com/materials/v1'
  
  # Builds url header information
  headers = {
    'Authorization': 'Bearer ' + access_token
  }

  # Gets material data
  materials_response = requests.get(url=api_url +'?', headers=headers)

  # Get a list of material keys
  keys = materials_response.json()['materials'].keys()
  
  # Get material id by material name
  # Loop through keys
  for key in keys:

    # Compare titles with each key
    if materials_response.json()['materials'][key]['title'] == material_name:
      
      # Return material id when match found
      return materials_response.json()['materials'][key]['materialId']

def submit_order(access_token, material_id, model_id, first_name, last_name, country_code, state_code, city, address1, address2, zipcode, phone_Number):
  """Submits a shipping order to 3D printing company API
  Args:
    access_token (str): 
    material_id (str): 
    model_id (str): 
    first_name (str): 
    last_name (str): 
    country_code (str): 
    state_code (str): 
    city (str): 
    address1 (str): 
    address2 (str): 
    zipcode (str): 
    phone_Number (str): 
  Returns:
    order_response (Dict): A dictoinary containing a 'result' status and a 'reason' discription
  """

  payment_verification_id =  os.getenv('PAYMENT_VERIFICATION_ID')
  # Url to retrieve material data
  api_url = 'https://api.shapeways.com/orders/v1'
  
  # Create item dictionary to purchase
  items = [{
    'materialId': material_id,
    'modelId': model_id,
    'quantity': 1
  }]

  # Create shipping order dictionary
  order_data = {
    'items': items,
    'firstName' : first_name,
    'lastName' : last_name,
    # Only 2 digits
    'country' : country_code,

    'state' : state_code,
    'city' : city,
    'address1' : address1,
    'address2' : address2,
    'zipCode' : zipcode,
    # Must be 10 digits for US numbers
    'phoneNumber' : phone_Number,
    'paymentVerificationId': payment_verification_id,
    'paymentMethod': 'credit_card',
    # 'Cheapest' or 'Fastest' are the only options
    'shippingOption': 'Cheapest'
  }

  # Builds url header information
  headers = {
    'Authorization': 'Bearer ' + access_token
  }
  
  # Post order and receive response
  order_response = requests.post(url=api_url, headers=headers, data=json.dumps(order_data))
  
  # Return response
  return order_response.json()
