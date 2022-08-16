# Pinata Pinner
The pinner prepares a set of images and associated metadata to be used for NFT minting. 
It will handle the following:
1. Upload a directory of images to [pinata](https://www.pinata.cloud/).
2. Records an association between the file name of the image and the ipfs url where the image was uploaded. Stored in a mongo db for easy retrieval.

This application is designed to process groups of images in the low thousands. It takes a few seconds per image, so, if you want to process massive numbers of images then 
you should extend this app to take advantage of parallel processing. If you do so, please make a pull request and we will happily incorporate it.


## Before using this utility you must have the following:
1. An account with [pinata](https://www.pinata.cloud/).
2. API keys for your pinata account. [Instructions here](https://knowledge.pinata.cloud/en/articles/6191471-how-to-create-an-pinata-api-key).
3. Install [docker](https://docs.docker.com/engine/install/) and `docker-compose` (comes with the desktop install).
4. A set of images you wish to upload to pinata


## Usage:
1. Clone this repo
2. Move all images you wish to pin into the directory `upload`. 
    Each set of images should be inside a subdirectory with a name identifying their collection.
    For example, for a collection named `SpacePuppies`, the images should be found at `pinata_pinner/upload/SpacePuppies`
3. From the `pinata_pinner` directory, run the command `PINATA_API_KEY=insertyourkeyhere docker-compose up`
    Replace 'insertyourkeyhere' in the above command with your pinata api jwt.

To view the data output by the app, simply connect to the mongo database. It will stay running until you
bring the compose down.
We recommend [mongodb compass](https://www.mongodb.com/try/download/compass) as a client.  The connection uri is: `mongodb://localhost:27019`

Since this information is stored in a database, you can integrate this into your larger business easily by connecting to the db and processing the information however you like.