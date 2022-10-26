import os
import requests
from requests.auth import HTTPBasicAuth

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
flow_token = os.getenv('FLOW_TOKEN')
twillio_number = os.getenv('TWILLIO_PHONE_NUMBER')

def lambda_handler(event, context):
    phone_number = event['request']['userAttributes']['phone_number']
    name = event['request']['userAttributes']['name']
    
    url = f'https://studio.twilio.com/v2/Flows/{flow_token}/Executions'

    
    payload = f'From={twillio_number}&To={phone_number}&Parameters={{"name":"{name}","phone_number": "{phone_number}"}}'

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.request('POST', url, auth=HTTPBasicAuth(account_sid, auth_token), headers=headers, data=payload)
    print(response)
    
    return event