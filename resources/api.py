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
