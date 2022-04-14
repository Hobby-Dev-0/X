import os
import sys
import heroku3
from telethon import TelegramClient
from telethon.sessions import StringSession
from .apivar import *

if SESSION is not None:
    session_name = str(SESSION)
    BaseClient = TelegramClient(StringSession(session_name), APP_ID, API_HASH)
else:
    session_name = "startup"
    BaseClient = TelegramClient(session_name, APP_ID, API_HASH)
