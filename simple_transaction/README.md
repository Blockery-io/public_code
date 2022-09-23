# Simple Transaction Builder
This app is designed to showcase how to create a simple transaction via blockery. 
In this app we simply move some ADA from one wallet to another. 

## Before using this utility you must have the following:
1. An account with [blockery.io](https://www.blockery.io/).
2. API keys for your blockery account. [Create Here](https://knowledge.pinata.cloud/en/articles/6191471-how-to-create-an-pinata-api-key).
3. Install [docker](https://docs.docker.com/engine/install/) and `docker-compose` (comes with the desktop install).

## Usage:
1. Clone this repo
2. From the `simple_transaction` directory, run the command `BLOCKERY_API_KEY=insertyourkeyhere BLOCKERY_API_URL=https://app-stage.blockery.io RECEIVE_ADDRESS=where_it_should_go AMOUNT=2000000 docker-compose up`
    * Replace 'insertyourkeyhere' in the above command with your blockery api jwt.
    * If you wish to use the main net instead of testnet, make sure to use `https://app.blockery.io` for `BLOCKERY_API_URL`.
3. To see the feedback from blockery about whether the transaction succeeds, watch your `request_results` event channel using the [pubsub](https://github.com/Blockery-io/public_code/tree/main/pubsub/python) app.
