import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

CHANNEL_LINK = "https://t.me/+htUvvtbDjdVhNDFl"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
👑 ABHISHEK KAR COMMUNITY 📊

Hello Trader 👋
Welcome to our Unofficial Educational Community.

📈 Market Learning
📚 Trading Education
📊 Market Updates
💡 Market Insights
🛡️ Risk Management

🎯 Learn • Analyze • Grow Together

👇 Join our Telegram Community

⚠️ Educational purposes only.
No guaranteed returns or assured profits.
This bot does not provide investment advice.

ℹ️ Unofficial community bot.
Not affiliated with or endorsed by Abhishek Kar.
"""

    keyboard = [
        [InlineKeyboardButton("📢 JOIN CHANNEL", url=CHANNEL_LINK)],
        [InlineKeyboardButton("📚 MARKET LEARNING", callback_data="learning")]
    ]

    await update.message.reply_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
