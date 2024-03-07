import logging
from decouple import config
import sys

# Logging Configuration
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)

# Variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None)
SUDO_USERS = set(int(user_id.strip()) for user_id in AUTH.split(',')) if AUTH else set()

# Bot Setup
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

userbot = Client("myacc", api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re-add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

try:
    Bot.start()
except Exception as e:
    logger.error(e)
    sys.exit(1)
