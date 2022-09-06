from pinata_pinner.app.pinata_pinner import run_pinner
from metadata_prepper.app.metadata_prepper import run_metadata_prepper
from nft_minter.app.nft_minter import run_minter
import os


if __name__ == "__main__":
    pinata_jwt = os.environ['PINATA_API_KEY']
    mongo_uri = os.environ['MONGO_URI']
    blockery_api_key = os.environ['BLOCKERY_API_KEY']
    nft_collection_name = os.environ['NFT_COLLECTION_NAME']
    blockery_api_url = os.environ['BLOCKERY_API_URL']
    run_pinner(pinata_jwt, mongo_uri)
    run_metadata_prepper(mongo_uri)
    run_minter(blockery_api_key, blockery_api_url, mongo_uri, nft_collection_name)