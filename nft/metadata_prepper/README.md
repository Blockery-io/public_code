# Metadata Prepper
The pinner prepares a set of images and associated metadata to be used for NFT minting. 
It will handle the following:
1. Upload a directory of images to [pinata](https://www.pinata.cloud/).
2. Records an association between the file name of the image and the ipfs url where the image was uploaded. Stored in a mongo db for easy retrieval.

This application is designed to process groups of images in the low thousands. It takes a few seconds per image, so, if you want to process massive numbers of images then 
you should extend this app to take advantage of parallel processing. If you do so, please make a pull request and we will happily incorporate it.


## Before using this utility you must have the following:
1. Install [docker](https://docs.docker.com/engine/install/) and `docker-compose` (comes with the desktop install).
2. A set of data structures you wish to use to define some nft metadata.


## Usage:
1. Clone this repo
2. Create metadata structures.
   1. Define these structures in discreet json files. For example, if you have 10 nfts to mint, there should be 10
   files with a `.json` extension.
   2. The structures should follow the schema defined in the [Blockery Public Api](https://app.blockery.io/docs/public-api/v1#tag/nft)
   Here is an example structure which conforms to the schema as of August 2022:
   ```
   {
      "name": "my_nft_name_001",
      "receive_address": "addr_test1qrm3hjh30x3ffh5u8jch5n53n76fxdazpg0ejnjtuzgqg70djpltrn262hjuw3mhv4dr3l6wyd2n2m6nw58xnfywqhxqfa6c60",
      "policy_id": "451882450d70e3ec27a87a6f3fe96514930af66aa85d8dac85a0bc6e",
      "quantity": 1,
      "metadata": {
        "name": "my_nft_name_001",
        "description": "This is a great asset we minted on blockery.io!",
        "mediaType": "image/png",
        "website": "https://blockery.io",
        "twitter": "https://twitter.com/blockery_io",
        "id": "001",
        "image": "ipfs://Qma5x12e8gUeydJ9qVNPTt63JvNYPppCyrJ2FBzXoscG3h",
        "files": [
          {
            "mediaType": "image/png",
            "src": "ipfs://Qma5x12e8gUeydJ9qVNPTt63JvNYPppCyrJ2FBzXoscG3h",
            "name": "my_nft_name_001"
          }
        ],
        "attributes": {
          "rarity": "common",
          "color": "blue"
        }
    }
   ```
   3. If you used the `pinata_pinner` app, name the `.json` files the same way you named the file corresponding to the image for the nft. 
   This will tell the `metadata_prepper` to automatically fill in the `image` and `files` fields in the above data structures using the information
    already stored in the mongodb.
   
        For example, if you had an image named `cool_image.png` uploaded by `pinata_pinner`, including here a file named `cool_image.json` will tell the metadata_prepper to check the mongodb for the `images` and `files` fields.
   4. If you used the `policy_creator` app, include the policy id you created in the `policy_id` field. A `policy_id` is required.
   
3. Move all json files you wish to use as nft definitions into the directory `upload`. 
    Each set of images should be inside a subdirectory with a name identifying their collection.
    For example, for a collection named `SpacePuppies`, the images should be found at `pinata_pinner/upload/SpacePuppies`
4. From the `pinata_pinner` directory, run the command `PINATA_API_KEY=insertyourkeyhere MONGO_URI=mongodb://mongodb:27017 docker-compose up`
    Replace 'insertyourkeyhere' in the above command with your pinata api jwt.

To view the data output by the app, simply connect to the mongo database. It will stay running until you
bring the compose down.
We recommend [mongodb compass](https://www.mongodb.com/try/download/compass) as a client.  The connection uri is: `mongodb://localhost:27019`

Since this information is stored in a database, you can integrate this into your larger business easily by connecting to the db and processing the information however you like.