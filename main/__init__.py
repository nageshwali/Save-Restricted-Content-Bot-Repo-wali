#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = config("22188582", default=None, cast=int)
API_HASH = config("3301a96bdc3742526fdec1f7d8081faf", default=None)
BOT_TOKEN = config("7084487133:AAEz-AKEC-RLL5HQxJPslb-eqJZyqgXYAc0", default=None)
SESSION = config("BQFSkiYAkAEbLwCvnyk4jBZV_gIZLIZIYz0HzkhtUB-sk6ohynNI7sieLsfvGipmJYXjcgaFTBJUD1D9uT4PmJz37DhoKGTuL8JFMQ7U8giLX8DMKUXTID1cQOz_LIH9MEiQRWXok8Z1ciT1dA0zLutRquSQOr5rfeikx5xUzJoe0C4FjPpodkn55TQmiF694HWyisMslHEEKgFepWujHKAYE1M5pBOw5W_vypoIgpatn0zgX_tGpmoB3Vt3dtxu1hFp2w0NE8J_AZ4PrL2fnGElfWNKCVgRue_5HTMfMIfvvlZpEh5GmEB5YGtiqwKbD6mDObaeIdyMj6QGq3p2H7JzLtFiQAAAAAAyAYYQAA", default=None)
FORCESUB = config("restrictedsaverr", default=None)
AUTH = config("838960656", default=None)
SUDO_USERS = []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
