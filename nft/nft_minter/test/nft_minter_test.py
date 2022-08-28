import unittest
import os
from app.nft_minter import run_minter
from pymongo import MongoClient
import random
import string


class MyTestCase(unittest.TestCase):
    def test_run_minter(self):
        '''
        This test populates a the mongo db with documents describing 40 NFTs. It then
        uses the nft minding function to mint those NFTs via blockery. The intention
        of this test is to provide a concrete example of the entire lifecycle from
        defining the NFTs in a database to actually minting them.
        :return:
        '''
        #prepare db
        mongo_url = "mongodb://mongodb:27017" #running in docker
        mongo_url = "mongodb://localhost:27019" #running outside docker
        mongo_client = MongoClient(mongo_url)

        db = mongo_client.blockery_public
        nft_collection_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

        os.environ['BLOCKERY_API_URL'] = "https://app-stage.blockery.io"
        os.environ['NFT_COLLECTION_NAME'] = nft_collection_name
        os.environ['MONGO_URI'] = mongo_url
        collection = db.nfts
        for i in range(40):
            nft_name = f'{nft_collection_name}{i}'
            collection.insert_one({
                'ipfs_uri': 'ipfs://QmWw9uCKktxt9DGtK6qYLRE7gWefSPsSjbUgvJGQsu84WQ',
                'nft_collection_name': nft_collection_name,
                'image_filename': 'blockery_banner.jpg',
                'nft_body': #This structure is used to fill out the blockery api call. Should comply with the spec here: https://app.blockery.io/docs/public-api/v1#tag/nft
                    {
                        "name": nft_name,
                        "receive_address": "addr_test1qrm3hjh30x3ffh5u8jch5n53n76fxdazpg0ejnjtuzgqg70djpltrn262hjuw3mhv4dr3l6wyd2n2m6nw58xnfywqhxqfa6c60",
                        "policy_id": "451882450d70e3ec27a87a6f3fe96514930af66aa85d8dac85a0bc6e",
                        "quantity": 1,
                        "metadata": {
                            "name": nft_name,
                            "description": "This is a great asset we minted on blockery.io!",
                            "mediaType": "image/png",
                            "website": "https://blockery.io",
                            "twitter": "https://twitter.com/blockery_io",
                            "id": f"{i}",
                            "image": "ipfs://QmWw9uCKktxt9DGtK6qYLRE7gWefSPsSjbUgvJGQsu84WQ",
                            "files": [
                                {
                                    "mediaType": "image/png",
                                    "src": "ipfs://QmWw9uCKktxt9DGtK6qYLRE7gWefSPsSjbUgvJGQsu84WQ",
                                    "name": nft_name
                                }
                            ],
                            "attributes": {
                                "rarity": "common",
                                "color": "blue"
                            }
                        }
                    }
            })

        run_minter()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
