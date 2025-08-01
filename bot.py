import os
import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Load your tokens from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# Function to get response from ChatGPT
def chatgpt_response(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Start command
def start(update, context):
    update.message.reply_text("👋 Welcome! I’m your AI accountability coach. Type /checkin to log progress or ask me anything.")

# Checkin command
def checkin(update, context):
    update.message.reply_text("📚 What did you study today?\nSend:\nTopic:\nTime:\n1 Takeaway:")

# MyWhy command
def mywhy(update, context):
    update.message.reply_text("🔥 WHY: To change your life through discipline and digital skills.")

# Quote command
def quote(update, context):
    update.message.reply_text("💡 'Discipline is choosing between what you want now and what you want most.'")

# Main AI message handler
def handle_message(update, context):
    user_input = update.message.text
    ai_reply = chatgpt_response(user_input)
    update.message.reply_text(ai_reply)

def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("checkin", checkin))
    dp.add_handler(CommandHandler("mywhy", mywhy))
    dp.add_handler(CommandHandler("quote", quote))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
