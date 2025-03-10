from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# Replace this with your bot token from BotFather
TOKEN = AAGGAett_CmxThf5-Ko-L43T3wyCXo_yhYU

# Define responses
def chat(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text.lower()
    responses = ["Hello!", "How are you?", "I'm a chatbot!", "Tell me more!"]
    update.message.reply_text(random.choice(responses))

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am your AI bot.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
