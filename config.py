# config.py - Complete version with all required variables

import os
import logging
from logging.handlers import RotatingFileHandler

# Bot configuration
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
APP_ID = int(os.environ.get("APP_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")

# Channel configuration
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "0"))
FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", "0")

# Owner/Admin
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
ADMINS = [OWNER_ID]

# Database - OPTIONAL (works without MongoDB)
DB_URI = os.environ.get("DATABASE_URI", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharingbot")

# Auto Delete Settings
AUTO_DELETE_TIME = int(os.environ.get("AUTO_DELETE_TIME", "0"))
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file will be deleted in {time} seconds")

# Messages
START_MSG = os.environ.get("START_MESSAGE", "Hello {first}!\n\nI can store files and give you a shareable link.")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Please join the channel first!")
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "")

# Settings
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False").lower() == "true"
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False").lower() == "true"

# Port for web server
PORT = int(os.environ.get("PORT", "8080"))

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "log.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
