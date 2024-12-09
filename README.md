# Haveloc Telegram Bot

The **Haveloc Telegram Bot** is a Python-based Telegram bot designed to assist users with various tasks and information related to Haveloc. This bot provides commands to check live status, manage registrations, and more. It integrates with Telegram and utilizes environment variables to manage bot configuration securely.

## Features

- **Start and Help Commands**: Provides basic information and assistance on how to use the bot.
- **Live Status Check**: Allows users to check the live status of services.
- **Registration and Management**: Commands to register, delete, and manage user registrations.
- 
## Docker Integration

This project includes Docker support, making it easy to containerize and run the bot. The Dockerfile sets up a Python environment and prepares the bot to be run in a Docker container.

## Prerequisites

- Python 3.x
- `python-telegram-bot` library (install via `pip install python-telegram-bot`)
- `dotenv` library (install via `pip install python-dotenv`)
