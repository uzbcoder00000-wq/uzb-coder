import os
import asyncio
from googletrans import Translator
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
from keep_alive import keep_alive

translator = Translator()
TOKEN = os.getenv("TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    translated = translator.translate(text, dest='uz')
    await update.message.reply_text(f"Tarjima: {translated.text}")

def main():
    keep_alive()
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()