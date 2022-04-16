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


EMOJI_PATTERN = re.compile(
    "["
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F700-\U0001F77F"  # alchemical symbols
    "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
    "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
    "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
    "\U0001FA00-\U0001FA6F"  # Chess Symbols
    "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
    "\U00002702-\U000027B0"  # Dingbats
    "]+"
)

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
