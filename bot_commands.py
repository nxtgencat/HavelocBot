from db import get_user_data, delete_user_data, register_user


async def start(update, context):
    """Handle /start command."""
    await update.message.reply_text(
        "Welcome to the bot! Use /help to see the available commands."
    )


async def help(update, context):
    """Handle /help command."""
    help_text = (
        "Here are the available commands:\n"
        "/live - Check status of bot\n"
        "/status - Check your shortlisted status\n"
        "/register <reg_number> - Register with your registration number\n"
        "/delete - Delete your data\n"
    )
    await update.message.reply_text(help_text)


async def live(update, context):
    """Handle /live command to check bot's status."""
    await update.message.reply_text("The bot is online and running.")


async def register(update, context):
    """Handle /register command."""
    chat_id = update.message.chat_id

    if len(context.args) < 1:
        await update.message.reply_text("Usage: /register <registration_number>")
        return

    # Get the registration number and convert it to uppercase
    reg_number = context.args[0].upper()  # Convert registration number to uppercase

    # Register or update user registration number in the database
    registration_successful = register_user(chat_id, reg_number)

    if registration_successful:
        await update.message.reply_text(
            f"Your registration number {reg_number} has been successfully registered."
        )
    else:
        await update.message.reply_text(
            "You have already registered a registration number. You can only register one."
        )


async def delete(update, context):
    """Handle /delete command."""
    chat_id = update.message.chat_id
    result = delete_user_data(chat_id)

    if result:
        await update.message.reply_text("Your data has been deleted from the system.")
    else:
        await update.message.reply_text("No data found for your account.")


async def status(update, context):
    """Handle /status command."""
    chat_id = update.message.chat_id
    user_data = get_user_data(chat_id)  # Retrieve user data from the database

    if user_data:
        reg_number, shortlisted_companies = user_data

        # Check if shortlisted_companies is None or empty
        if shortlisted_companies:
            status_message = f"Your registration number: {reg_number}\nShortlisted Companies: {', '.join(shortlisted_companies)}"
        else:
            status_message = f"Your registration number: {reg_number}\nShortlisted Companies: No data available"
    else:
        status_message = "No data found.\nPlease register first using /register <registration_number>."

    await update.message.reply_text(status_message)