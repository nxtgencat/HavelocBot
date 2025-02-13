import logging
import sys

def setup_logger():
    """Configure and return a logger instance for the Telegram bot."""
    # Create a custom stream handler for console output
    console_handler = logging.StreamHandler(sys.stdout)  # Use stdout instead of stderr
    console_handler.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler("haveloc_bot.log")
    file_handler.setLevel(logging.INFO)

    # Create formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Add formatter to handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Get the root logger and configure it
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Remove any existing handlers
    logger.handlers.clear()

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# Create a logger instance that can be imported by other modules
logger = setup_logger()