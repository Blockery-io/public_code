import os
import requests


def simple_transaction(receive_address, amount, blockery_api_token, base_url):
    '''
    :return:
    '''

    route = '/api/v1/transaction'

    url = base_url + route

    tx_body = {
        "user_specified_id": "my_arbitrary_string",
        "outputs": [
            {
                "receive_address": receive_address,
                "lovelace_amount": int(amount)
            }
        ]
    }
    response = requests.post(url=url, json=tx_body, headers={'Authorization': f'Bearer {blockery_api_token}'})
    if not response.ok:
        raise Exception(response.content)

if __name__ == "__main__":
    blockery_api_token = os.environ['BLOCKERY_API_KEY']
    base_url = os.environ['BLOCKERY_API_URL']
    receive_address = os.environ['RECEIVE_ADDRESS']
    amount = os.environ['AMOUNT']
    simple_transaction(receive_address, amount, blockery_api_token, base_url)