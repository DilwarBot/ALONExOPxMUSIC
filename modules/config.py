import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ALONE_WAS_BOT")
SUPPORT_GROUP = getenv("SUPPORT_GROUP","ALONE_CHATTING_WORLD")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL","ALONE_CHATTING_WORLD")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1282754256").split()))
aiohttpsession = aiohttp.ClientSession()
