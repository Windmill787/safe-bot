from telethon import TelegramClient, events, sync
import os
from telegram import Update, Bot
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import re
import json

client = TelegramClient('session_name', os.getenv('API_ID'), os.getenv('API_HASH'))
client.start()

bot = Bot(token=os.getenv('BOT_KEY'))

my_id = client.get_me().id
channel_matches = json.loads(os.environ['CHANNELS'])

channel_ids = []
for dialog in client.get_dialogs():
    for match in channel_matches:
        if re.search(match, dialog.name, re.IGNORECASE):
            channel_ids.append(dialog.message.peer_id.channel_id)


@client.on(events.NewMessage(chats=channel_ids))
async def send_message(event):
    message_matches = json.loads(os.environ['MESSAGES'])
    for message_match in message_matches:
        if re.search(message_match, event.message.message, re.IGNORECASE):
            text = event.message.message
            if event.message.reply_to is not None:
                reply = await client.get_messages(event.message.peer_id, ids=event.message.reply_to.reply_to_msg_id)
                text = "Reply to \"%s\": %s" % (reply.message, event.message.message)
            await bot.send_message(chat_id=my_id, text=text)

if __name__ == '__main__':
    client.run_until_disconnected()
    print('Client is running')
