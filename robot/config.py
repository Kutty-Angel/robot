#
# Copyright (C) by Kutty-Angel@Github, < https://github.com/Kutty-Angel >.
#
# This file is part of < https://github.com/Kutty-Angel/robot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kutty-Angel/robot/blob/main/LICENSE >
#
# All rights reserved !!


from os import getenv
from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSID = int(getenv("ASSID"))
ASSNAME = getenv("ASSNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID", "5338869949"))
UPDATE = getenv("UPDATE", "DuskyBotZUpdates")
SUPPORT = getenv("SUPPORT", "DuskyBotZSupport")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9999"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/f2a2d31f60a9e0f3dbe94.png")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5338869949").split()))
START_PIC = getenv("START_PIC", "https://telegra.ph/file/4935b94ee534ac94319ad.png")
OWNER_USERNAME = getenv("OWNER_USERNAME")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/4935b94ee534ac94319ad.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/4935b94ee534ac94319ad.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/4935b94ee534ac94319ad.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/4935b94ee534ac94319ad.jpg")
