This app is an example of using the pubnub sdk to subscribe to blockery event channels. 
For example, the `request_response` channel provides your organization information related to requests you make to the api.

See your organization dashboard for getting the subscribe key, auth key, and channel.

## Usage

Bring it up by replacing the placeholder values in the below command with your real values:

`SUBSCRIBE_KEY=yoursubscribekey UUID=youruuid AUTH_KEY=pubnubkey CHANNEL_NAME=yourchannelname docker-compose up`


Explanation of the env vars:

      SUBSCRIBE_KEY: "yourkey" (Get this on your org dashboard)
      UUID: "youruuid" (An arbitrary value you can set to identify your app. Set to anything)
      AUTH_KEY: "authkey" (Generate one of these via the Generate Token PubNub at https://app.blockery.io/organizations)
      CHANNEL_NAME: "12345_request_results" (Get this on your org dashboard)

You will now see messages streamed to the console when you make use of the public API at blockery.io