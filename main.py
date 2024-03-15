from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, filters, ContextTypes

TOKEN: Final = '6331974262:AAFBC5_9bmT-iySBi-2rmu7SElcvwmWAXHc'
BOT_USERNAME: Final = '@cutiest1703_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Kristina Imperatrica!')

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=1)

