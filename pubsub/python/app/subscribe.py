from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from app.subscribe_callback import MySubscribeCallback
import os

pnconfig = PNConfiguration()
pnconfig.subscribe_key = os.environ['SUBSCRIBE_KEY']
pnconfig.uuid = os.environ['UUID']  # arbitrary value. used to identify the app.
pnconfig.auth_key = os.environ['AUTH_KEY']
pubnub = PubNub(pnconfig)
pubnub.add_listener(MySubscribeCallback())
channel_name = os.environ['CHANNEL_NAME']
print(f'Subscribing to channel <{channel_name}> with the following configuration:\n'
      f'Subscribe key: <{os.environ["SUBSCRIBE_KEY"]}>\n'
      f'UUID: <{os.environ["UUID"]}>\n'
      f'AUTH_KEY: <{os.environ["AUTH_KEY"]}>')
pubnub.subscribe().channels(os.environ['CHANNEL_NAME']).execute()
print('test')