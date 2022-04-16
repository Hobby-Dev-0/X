import asyncio
import math
import os
import sys
import re
import heroku3
import requests
import urllib3
union = os.environ.get
version = union("UB_VER")
ver = "0.1"
async def checkup():
  if version != ver:
    print ("Version Can't Match Please Update the bot or contact support")
    sys.exit()
  else:
    pass

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)

SESSION = union("SESSION")
APP_ID = API_ID = union("API_ID")
API_HASH = union("API_HASH")
ENV = union("ENV", False)
ALIVE_NAME = union("ALIVE_NAME") or "Please set Your Name on Heroku or Railway in vars section"
BLOCKLIST = union("BLOCKLIST", "")
HANDLER = union("HANDLER")
SUDO_HANDLER = union("SUDO_HANDLER")
BOT_USERNAME = union("BOT_USERNAME")
BOT_TOKEN = union("BOT_TOKEN")
SUDO_CLIENT = set(int(x) for x in union("SUDO_USERS", "").split())
