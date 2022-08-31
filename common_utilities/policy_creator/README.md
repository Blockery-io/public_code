# Policy Creator
The app will create a policy at blockery.io attached to your organization. You can then use that policy in the future for minting nfts, tokens, or anything else a policy is useful for.

It will handle the following:
1. Sends environment variables to the Blockery Public API in order to create a policy 
2. Stores information about the policy in a local mongo database.


## Before using this utility you must have the following:
1. An account with [blockery.io](https://www.blockery.io/).
2. API keys for your blockery account. [Create Here](https://knowledge.pinata.cloud/en/articles/6191471-how-to-create-an-pinata-api-key).
3. Install [docker](https://docs.docker.com/engine/install/) and `docker-compose` (comes with the desktop install).


## Usage:
1. Clone this repo
2. From the `policy_creator` directory, run the command `BLOCKERY_API_KEY=insertyourkeyhere BLOCKERY_API_URL=https://app-stage.blockery.io/ docker-compose up`
   * Add the environment variable `SLOT_EXPIRY` if you want the policy to expire at a specific slot. Set the value to the slot number at which you want the policy to expire.
   * Add the environment variable `EXPIRES_IN` if you want the policy to expire in a certain number of slots from now. On average, one slot is roughly equal to one second.
   * Replace 'insertyourkeyhere' in the above command with your blockery api jwt.
   * If you wish to use the main net instead of testnet, make sure to use `https://app.blockery.io/` for `BLOCKERY_API_URL`.


To view the data output by the app, simply connect to the mongo database. It will stay running until you
bring the compose down.
We recommend [mongodb compass](https://www.mongodb.com/try/download/compass) as a client.  The connection uri is: `mongodb://localhost:27019`

Since this information is stored in a database, you can integrate this into your larger business easily by connecting to the db and processing the information however you like.