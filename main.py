import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler
from bot_commands import start, help, live, status, register, delete
from logger import logger

# Load environment variables from .env file
load_dotenv()

# Get the bot token from environment variables
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")


def run_bot():
    """Run the bot with webhook settings."""

    # Create the application instance
    application = Application.builder().token(bot_token).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("live", live))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(CommandHandler("register", register))
    application.add_handler(CommandHandler("delete", delete))

    # Run the bot
    application.run_polling()


run_bot()