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
pubnub.subscribe().channels(os.environ['CHANNEL_NAME']).execute()
