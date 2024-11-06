import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()  # Load environment variables from .env file
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token:
        raise ValueError("Bot token is not set in the environment variables.")

    return bot_token
