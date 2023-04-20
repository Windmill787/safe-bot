from telethon import TelegramClient, events, sync
import os
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

client = TelegramClient('session_name', int(os.getenv('API_ID')), os.getenv('API_HASH'))
client.start()

my_id = client.get_me().id

bot = Bot(token=os.getenv('SAFE_BOT_KEY'))

# TODO: set chats ids
@client.on(events.NewMessage(chats=[my_id]))
async def send_message(event):
    # TODO: check matches
    await bot.send_message(chat_id=my_id, text='Hello')

if __name__ == '__main__':
    client.run_until_disconnected()
