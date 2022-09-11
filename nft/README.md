This directory contains helper utilities related to minting NFTs.

Utilities:

* `pinata_pinner` - Upload images to the ipfs service "pinata" for use in NFTs.
* `metadata_prepper` - Prepares the metadata to be used by `nft_minter` for minting the nfts.
* `nft_minter` - Mint NFTs using the Blockery API. Uses mongo entries from `pinata_pinner` and `metadata_prepper` as input.
* `end_to_end` - This script will run all other utilities as an end-to-end package.


## End_to_End

This little script assumes you want to create one or more nfts with images. If you aren't creating nfts with images, or you
have some complexity that isn't easily dealt with here, we encourage you to fork this repo and modify it in whatever manner
suits your needs.

### Requirements
You must have the following before using the app.
1. An account with [pinata](https://www.pinata.cloud/).
2. API keys for your pinata account. [Instructions here](https://knowledge.pinata.cloud/en/articles/6191471-how-to-create-an-pinata-api-key).
3. Install [docker](https://docs.docker.com/engine/install/) and `docker-compose` (comes with the desktop install).
4. A set of images you wish to upload to pinata. Place these in `pinata_pinner.upload`. An example is already present for you.
5. A set of data structures you wish to use to define some nft metadata. Place these in `metadata_prepper.upload` in `.json` format. An example is already present for you.
<br>**Note**: Make sure the `policy_id` is a policy id associated with your org. To easily create a new policy for your org you can either use the [policy resource](https://app.blockery.io/docs/public-api/v1#tag/policy) on the api or you can use our [helper app](https://github.com/Blockery-io/public_code/tree/main/common_utilities/policy_creator).
6. An account with [blockery.io](https://www.blockery.io/).
7. API keys for your blockery account. [Create Here](https://app.blockery.io/organization).

### Usage
1. Clone this repo
2. From the `nft` directory, run the command `PINATA_API_KEY=insertyourkeyhere BLOCKERY_API_KEY=insertyourkeyhere BLOCKERY_API_URL=https://app-stage.blockery.io NFT_COLLECTION_NAME=directory_name_images_are_inside_within_upload_folder docker-compose up`
    Replace placeholders in the above with appropriate values.
3. Once you see the log message `nft_end_to_end_app_1 exited with code 0` the program is complete. You can now safely shut down the compose with `cntrl + c` or whichever command is appropriate on your os.
