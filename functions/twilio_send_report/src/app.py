import os
import requests
from datetime import date
from requests.auth import HTTPBasicAuth

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')
FLOW_TOKEN = os.getenv('FLOW_TOKEN')
TWILLIO_PHONE_NUMBER = os.getenv('TWILLIO_PHONE_NUMBER')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_REGION = os.getenv('AWS_REGION')

def lambda_handler(event, context):
    user_whatsapp = event['SUBS_GSI_PK']['S'].replace('USER#', '')
    stock = event['PK']['S'].replace('SUBSCRIPTION#', '')

    today = date.today()
    url = f'https://studio.twilio.com/v2/Flows/{FLOW_TOKEN}/Executions'

    report_path = f'https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com/{stock}-{today}.csv'
    payload = f'From={TWILLIO_PHONE_NUMBER}&To={user_whatsapp}&Parameters={{"report":"{report_path}"}}'

    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    response = requests.request('POST', url, auth=HTTPBasicAuth(ACCOUNT_SID, AUTH_TOKEN), headers=headers, data=payload)
    print(response)
    
    return event