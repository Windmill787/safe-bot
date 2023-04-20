from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import os


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Success')

if __name__ == '__main__':
    application = ApplicationBuilder().token(os.getenv('SAFE_BOT_KEY')).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()
