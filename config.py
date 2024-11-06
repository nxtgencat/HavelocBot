import os

from dotenv import load_dotenv


def load_config():
    # Load environment variables from .env file
    load_dotenv()

    # Load Telegram Bot Token
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not bot_token:
        raise ValueError("Bot token is not set in the environment variables.")

    # Load Supabase credentials
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    if not supabase_url or not supabase_key:
        raise ValueError("Supabase URL or key is not set in the environment variables.")

    # Return both bot token and Supabase credentials
    return bot_token, supabase_url, supabase_key
