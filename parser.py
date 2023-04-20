from telethon import TelegramClient, events, sync
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

client = TelegramClient('session_name', os.getenv('API_ID'), os.getenv('API_HASH'))
client.start()

myId = client.get_me().id

application = ApplicationBuilder().token(os.getenv('SAFE_BOT_KEY')).build()

#application.bot.send_message(chat_id=myId, text='Hello')
