const PubNub = require('pubnub')

const pubnub = new PubNub({
    subscribeKey: process.env.PUBNUB_SUBSCRIBE_KEY,
    uuid: process.env.PUBNUB_UUID,
    authKey: process.env.PUBNUB_AUTH_KEY
})
pubnub.addListener({
    status: async function (statusEvent) {
        console.log(statusEvent)
        if (statusEvent.category === "PNConnectedCategory") {
            console.log("Connected to PubNub!")
        }
        else{
            console.log(statusEvent)
        }
    },
    message: function(message) {
        console.log(message)
    },
    presence: function (presenceEvent) {
       console.log(presenceEvent)
      },
})
pubnub.subscribe({
    channels: [`${process.env.PUBNUB_CHANNEL}`],
    authKeys:[`${process.env.PUBNUB_AUTH_KEY}`]
})