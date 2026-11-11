import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
ADMIN_CHAT_ID_VALUE = os.getenv("ADMIN_CHAT_ID", "").strip()

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Add it to your .env file.")

try:
    ADMIN_CHAT_ID = int(ADMIN_CHAT_ID_VALUE)
except ValueError as error:
    raise RuntimeError("ADMIN_CHAT_ID must be a valid integer in your .env file.") from error
