import logging
from telegram.ext import Application, CommandHandler
from bot_commands import start, help, live, status, register, delete
from config import load_config

# Setup logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def run_bot():
    """Run the bot with webhook settings."""
    # Get only the Telegram Bot Token
    bot_token, _, _ = load_config()

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
