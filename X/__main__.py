from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from . import *
from .main.botloader import modules_loading
import telethon.utils



async def add_bot(bot_token):
    await BaseClient.start(bot_token)
    BaseClient.me = await BaseClient.get_me() 
    BaseClient.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    BaseClient.disconnect()
else:
    BaseClient.tgbot = None
    if BOT_USERNAME is not None:
        print("Speedo USERBOT STABLE VERSION STARTING")
        BaseClient.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=API_ID,
            api_hash=API_HASH
        ).start(bot_token=BOT_TOKEN)
        print("X Started!")
        BaseClient.loop.run_until_complete(add_bot(BOT_USERNAME))
        print("Loading Software Completed")
    else:
        BaseClient.start()
        
BaseClient.loop.run_until_completed(modules_loading())
        
if len(argv) not in (1, 3, 4):
    BaseClient.disconnect()
else:
    BaseClient.run_until_disconnected()
