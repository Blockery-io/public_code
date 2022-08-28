import os

import requests
from pymongo import MongoClient

def run_minter():
    mongo_client = MongoClient(os.environ['MONGO_URI'])
    db = mongo_client.blockery_public
    nft_collection_name = os.environ['NFT_COLLECTION_NAME']

    collection = db.nfts
    unprocessed_nfts_remain = True
    page = 0
    total_processed_nfts = 0

    nft_transaction_body = {
	"user_specified_id": "ubilmat",
	"assets_to_mint": []
    }


    while unprocessed_nfts_remain: # here we iterate over all nfts in the db and mint them 40 at a time. Doing many at a time saves onchain transaction fees.
        result = collection.find({"nft_collection_name": nft_collection_name}).skip(page*40).limit(40)
        total_results = 0
        for nft in result:
            total_results += 1
            nft_transaction_body["assets_to_mint"].append(nft['nft_body'])
            if len(nft_transaction_body["assets_to_mint"]) >= 40:
                mint_nfts(nft_transaction_body)

        page += 1
        if total_results< 10: # we've reached the end of the pages of nft objects from the database, so let's mint that last batch even if there are less than 40
            unprocessed_nfts_remain = False
            if len(nft_transaction_body["assets_to_mint"]) >= 0:
                mint_nfts(nft_transaction_body)

    print(f'Total processed nfts: {total_processed_nfts}')

def mint_nfts(nft_body):
    '''
    Executes a single nft minting transaction which may contain a plurality of nfts.
    :param nft_body:
    :return:
    '''
    base_url = os.environ['BLOCKERY_API_URL']
    route = '/api/v1/nft'
    blockery_api_token = os.environ['BLOCKERY_API_KEY']
    url = base_url + route
    response = requests.post(url=url, json=nft_body, headers={'Authorization': f'Bearer {blockery_api_token}'})
    if not response.ok:
        raise Exception(response.json())

if __name__ == "__main__":
    run_minter()