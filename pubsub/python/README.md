This app is an example of using the pubnub sdk to subscribe to blockery response channels. Your organizatio receives information related to requests you make in a response channel.

See your organization dashboard for getting the subscribe key, auth key, and channel.

## Setup

Modify `docker-compose.yml` by inserting appropriate values for the following environment variables: 

      SUBSCRIBE_KEY: "yourkey" (Get this on your org dashboard)
      UUID: "youruuid" (Get this on your org dashboard)
      AUTH_KEY: "authkey" (Generate one of these via the Generate Token PubNub at https://app.blockery.io/organizations)
      CHANNEL_NAME: "12345_request_results" (Get this on your org dashboard)

## Usage

After setting up the env vars, bring it up:

`docker-compose up
` 

You will now see message streamed to the console when you make use of the public API at blockery.io
