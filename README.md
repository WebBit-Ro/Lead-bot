# Telegram Lead-Generation Quiz Bot

A lightweight Telegram lead-generation bot built with Python 3.11+, aiogram 3.x, and in-memory FSM storage. No external database is required.

## Setup

1. Create and activate a virtual environment, then install the dependencies:

   ```bash
   python -m venv .venv
   ```

   Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:

   ```bash
   source .venv/bin/activate
   ```

   Install packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Copy `.env.example` to `.env` and set your Telegram bot token and numeric admin chat ID:

   ```env
   BOT_TOKEN=your_telegram_bot_token
   ADMIN_CHAT_ID=123456789
   ```

3. Start the bot:

   ```bash
   python main.py
   ```

The bot sends each completed lead directly to `ADMIN_CHAT_ID`. Quiz progress is stored in memory and resets when the bot restarts.
