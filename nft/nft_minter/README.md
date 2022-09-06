# NFT Minter
The NFT Minter is designed to interface with the blockery API. It will mint a number of NFTs.
It will handle the following:
1. Mint NFTs defined in a local mongo database.
2. Uses the images uploaded by the blockery project [Pinata Pinner](https://github.com/Blockery-io/public_code/tree/main/nft/pinata_pinner)
3. Uses NFT descriptions prepared by the blockery project [Metadata Prepper](https://github.com/Blockery-io/public_code/tree/main/nft/metadata_prepper)

## Before using this utility you must have the following:
1. An account with [blockery.io](https://www.blockery.io/).
2. API keys for your blockery account. [Create Here](https://knowledge.pinata.cloud/en/articles/6191471-how-to-create-an-pinata-api-key).
3. Install [docker](https://docs.docker.com/engine/install/) and `docker-compose` (comes with the desktop install).
4. Mongodb containing descriptions of the nfts you wish to mint. 
    * You can use the [Pinata Pinner](https://github.com/Blockery-io/public_code/tree/main/nft/pinata_pinner) project to create these descriptions.
    * You can use [Metadata Prepper](https://github.com/Blockery-io/public_code/tree/main/nft/metadata_prepper) to fill out the entries created by Pinata Pinner with full descriptions.

## Usage:
1. Clone this repo
2. Prepare a collection in mongo with the collection name `nfts`. The documents in the collection should conform to the following structure:
```
{
                'ipfs_uri': 'ipfs://QmWw9uCKktxt9DGtK6qYLRE7gWefSPsSjbUgvJGQsu84WQ',
                'nft_collection_name': 'build',
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
                            "id": i,
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
            }
```

3. From the `nft_minter` directory, run the command `BLOCKERY_API_KEY=insertyourkeyhere BLOCKERY_API_URL=https://app-stage.blockery.io docker-compose up`
    * Replace 'insertyourkeyhere' in the above command with your blockery api jwt.
    * If you wish to use the main net instead of testnet, make sure to use `https://app.blockery.io` for `BLOCKERY_API_URL`.

As the app processes nfts, it will mark the documents with a timestamp under the field `nft_submitted`. 
To view the data output by the app, simply connect to the mongo database. It will stay running until you
bring the compose down.
We recommend [mongodb compass](https://www.mongodb.com/try/download/compass) as a client.  The connection uri is: `mongodb://localhost:27019`

Since this information is stored in a database, you can integrate this into your larger business easily by connecting to the db and processing the information however you like.