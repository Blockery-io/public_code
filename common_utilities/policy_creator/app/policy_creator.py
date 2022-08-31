import os
import requests
from pymongo import MongoClient


def create_policy(base_url, blockery_api_token, slot_expiry, expires_in):

    route = '/api/v1/policy'
    url = base_url + route
    body = {
        "name": "our_fav_policy",
        # "slot_expiry": 43827742,
        # "expires_in": 10000
        }

    if slot_expiry:
        body['slot_expiry'] = slot_expiry
        

    if expires_in:
        body['expires_in'] = expires_in

    response = requests.post(url=url, json=body, headers={'Authorization': f'Bearer {blockery_api_token}'})
    if not response.ok:
        raise Exception(response.json())

    mongo_url = "mongodb://localhost:27019" #running outside docker
    mongo_client = MongoClient(mongo_url)

    db = mongo_client.blockery_public
    collection = db.policy
    collection.insert_one({
        'policy_id': response.json()
    })


if __name__ == "__main__":
    base_url = os.environ['BLOCKERY_API_URL']
    blockery_api_token = os.environ['BLOCKERY_API_KEY']
    slot_expiry = os.environ.get('SLOT_EXPIRY', False)
    expires_in = os.environ.get('EXPIRES_IN', False)
    create_policy(base_url, blockery_api_token, slot_expiry, expires_in)