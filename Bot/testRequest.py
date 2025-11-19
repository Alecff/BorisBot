import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
import json

load_dotenv()
pw = os.environ.get('PW')

def createClaim(email, name):
    response = requests.post(
        "https://hub-opia-cloud.dev.opiahost.co.uk/api/v1/contact",
        json={
            "promotion_id": '2e77d3e2-b5ff-467b-852c-f098e2f625ef',
            "email": email,
            "first_name": name,
            "last_name": " ",
            "address": {
                "country": 'UK'
            },
        },
        headers={
            "Authorization": "Bearer " + os.environ.get('PW')
        },   
  )

    data = json.loads(response.text)
    contact_id = data['data']['contact']['id']
    print(contact_id)

    response = requests.post(
        "https://hub-opia-cloud.dev.opiahost.co.uk/api/v1/claim",
        json={
            "contact_id": contact_id,
        },
        headers={
            "Authorization": "Bearer " + os.environ.get('PW')
        },  
    )

    data = json.loads(response.text)
    return data['data']['claim']['public_reference']
