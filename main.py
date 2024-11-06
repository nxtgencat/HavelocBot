import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import json
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Store user data
user_data = {}

# Load existing user data if available
if os.path.exists("user_data.json"):
    with open("user_data.json", "r") as f:
        user_data = json.load(f)


# Save user data to a JSON file
def save_user_data():
    with open("user_data.json", "w") as f:
        json.dump(user_data, f)
    logger.info("User data saved to file.")


# Handle /start command and show options
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! Choose an action:\n"
        "/register - Register your registration number\n"
        "/delete - Delete your registration"
    )
    logger.info(f"User {update.message.chat_id} started the bot.")


# Handle /register command
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    if chat_id in user_data.values():
        # If the user is already registered, show their registration number
        reg_number = next(key for key, value in user_data.items() if value == chat_id)
        await update.message.reply_text(f"You are already registered with registration number: {reg_number}")
        logger.info(f"User {chat_id} tried to register again, already registered with {reg_number}.")
    else:
        # Ask for registration number
        await update.message.reply_text("Please enter your registration number:")
        logger.info(f"User {chat_id} is attempting to register.")

        # Save the user's registration number after they provide it
        async def registration_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
            reg_number = update.message.text.strip()
            # Store the registration number and chat ID
            user_data[reg_number] = chat_id
            save_user_data()
            context.application.remove_handler(registration_handler)  # Remove handler after registration

            # Use await properly to prevent the runtime warning
            await update.message.reply_text(f"Thank you! You've registered with registration number: {reg_number}")
            logger.info(f"User {chat_id} successfully registered with registration number: {reg_number}")

        # Add the message handler to wait for the registration number input
        context.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, registration_handler))


# Handle /delete command
async def delete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    reg_number = next((key for key, value in user_data.items() if value == chat_id), None)

    if reg_number:
        # Delete the registration number
        del user_data[reg_number]
        save_user_data()
        await update.message.reply_text(f"Your registration with number {reg_number} has been deleted.")
        logger.info(f"User {chat_id} deleted their registration number: {reg_number}")
    else:
        await update.message.reply_text("You are not registered. Use /register to register.")
        logger.info(f"User {chat_id} attempted to delete, but was not registered.")


def main():
    # Get the bot token from environment variables
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token:
        raise ValueError("The bot token is not set in the environment variables.")

    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("register", register))
    application.add_handler(CommandHandler("delete", delete))

    application.run_polling()  # Run the bot with polling


if __name__ == "__main__":
    main()
