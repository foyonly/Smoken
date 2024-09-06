from telethon.sync import TelegramClient
from telethon import functions, types
import json
import time
from datetime import datetime
config = json.load(open("config.json", encoding="utf-8"))
channels = open("channels.txt", encoding="utf-8").read().splitlines()
def start():
    for i in channels:
      try:
        fromPeer = config["messageToForward"].replace("https://t.me/", "").spli>
        id = config["messageToForward"].replace("https://t.me/", "").split("/")>
        toPeer = i.replace("https://t.me/", "").split("/")[0]
        topId = i.replace("https://t.me/", "").split("/")[1]
        try:
          with TelegramClient(config["name"], config["api_id"], config["api_has>
            client(functions.messages.ForwardMessagesRequest(
                from_peer=fromPeer,
                id=[int(id)],
                to_peer=toPeer,
                top_msg_id=int(topId),
            ))
            c = datetime.now().strftime("%H:%M:%S")
            print(f"[{c}] - Sent message to {toPeer}")
        except:
          continue
      except:
        fromPeer = config["messageToForward"].replace("https://t.me/", "").spli>
        id = config["messageToForward"].replace("https://t.me/", "").split("/")>
        toPeer = i.replace("https://t.me/", "").split("/")[0]
        try:
          with TelegramClient(config["name"], config["api_id"], config["api_has>
            client(functions.messages.ForwardMessagesRequest(
                from_peer=fromPeer,
                id=[int(id)],
                to_peer=toPeer,
            ))
            c = datetime.now().strftime("%H:%M:%S")
            print(f"[{c}] - Sent message to {toPeer}")
        except:
          continue
def run():
   while True:
    start()
    time.sleep(config["time"])
run()