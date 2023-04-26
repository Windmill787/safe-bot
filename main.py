from telethon import TelegramClient, events, sync
import os
from telegram import Update, Bot
import re
import sys

client = TelegramClient('session_name', os.getenv('API_ID'), os.getenv('API_HASH'))
client.start()

bot = Bot(token=os.getenv('BOT_KEY'))

my_id = client.get_me().id
channel_matches = sys.argv[1].split(',')
message_matches = sys.argv[2].split(',')

# print(channel_matches)
# print(message_matches)

channel_ids = []
for dialog in client.get_dialogs():
    for match in channel_matches:
        if re.search(match, dialog.name, re.IGNORECASE):
            if hasattr(dialog.message.peer_id, 'channel_id'):
                channel_ids.append(dialog.message.peer_id.channel_id)
            elif hasattr(dialog.message.peer_id, 'chat_id'):
                channel_ids.append(dialog.message.peer_id.chat_id)
            else:
                print('No chat_id or channel_id attribute')
                print(dialog)
                exit()

channel_ids.append(my_id)

@client.on(events.NewMessage(chats=channel_ids))
async def send_message(event):
    result_text = ''
    # print(event.message.message)
    reply_to_message = None
    if event.message.reply_to is not None:
        reply_to_message = await client.get_messages(event.message.peer_id, ids=event.message.reply_to.reply_to_msg_id)

    if reply_to_message is not None:
        reply_matches = False
        for message_match in message_matches:
            if re.search(message_match, reply_to_message.message, re.IGNORECASE):
                reply_matches = True
                break
        if not event.message.message.endswith('?'):
            for message_match in message_matches:
                if re.search(message_match, event.message.message, re.IGNORECASE) or reply_matches:
                    result_text = f'Reply to: "{reply_to_message.message}" <b>{event.message.message}</b>'
                    break
    else:
        if not event.message.message.endswith('?'):
            for message_match in message_matches:
                if re.search(message_match, event.message.message, re.IGNORECASE):
                    result_text = re.sub(message_match, f'<b>{message_match}</b>', event.message.message, flags=re.IGNORECASE)
                    break

    if result_text:
        await bot.send_message(chat_id=my_id, text=result_text, parse_mode='html')
if __name__ == '__main__':
    print('(Press Ctrl+C to stop script)')
    client.run_until_disconnected()
