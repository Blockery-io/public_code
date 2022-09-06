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

        collection = db.nfts
        for i in range(35):
            nft_name = f'{nft_collection_name}{i}'
            collection.insert_one({
                'ipfs_uri': 'ipfs://QmWw9uCKktxt9DGtK6qYLRE7gWefSPsSjbUgvJGQsu84WQ',
                'nft_collection_name': nft_collection_name,
                'image_filename': 'blockery_banner.jpg',
                'nft_body': #This structure is used to fill out the blockery api call. Should comply with the spec here: https://app.blockery.io/docs/public-api/v1#tag/nft
                    {
                        "name": nft_name,
                        "receive_address": "addr_test1qrpzs98ufjr6kw6nz60dcsf2eysaatvxu5aqwa0gn9ttmluk37rh6k3fddxqvhxa25yamn5keq6wpgfyndaadv7pyh6qe0y5ph",
                        "policy_id": "3c06a87f05836e53f375019d9cde2a64e94b5f53381f7af913ef2990",
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

        run_minter(os.environ['BLOCKERY_API_KEY'], "https://app-stage.blockery.io", mongo_url, nft_collection_name )
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
