"""
This module is for genearating session string, which is required to run a bot in Telegram.
"""

import asyncio
import os
from pyrogram import Client
from dotenv import load_dotenv


async def main():
    api_id, api_hash, bot_token = os.getenv("API_ID"), os.getenv("API_HASH"), os.getenv("BOT_TOKEN")
    async with Client("bot_session", api_id, api_hash, bot_token=bot_token) as app:  # Connecting to the bot
        session_string = await app.export_session_string()
        # copy this string and past it in '.env' file
        # you will find session string printed in terminal 
        print("Here is your session string:\n", session_string)


load_dotenv()
asyncio.run(main())
