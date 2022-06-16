from pubnub.pubnub import SubscribeCallback, PNStatusCategory


class MySubscribeCallback(SubscribeCallback):
    def __init__(self):
        print('initialized')
    def status(self, pubnub, status):
        print(f'status code: {status.category}')
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            print('Connectivity Lost')
            # This event happens when radio / connectivity is lost
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            print(f'Connected to {status.affected_channels}')
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            print('Connectivity Restored')
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            print('Decryption error detected')
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.

    def message(self, pubnub, message):
        # Handle new message stored in message.message
        print(message.message)
