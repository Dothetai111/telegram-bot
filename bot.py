from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8864131301:AAFL7530RArzvh22_gDK1g4QMw6zvfKWgIo"
WEBHOOK_URL = "https://your-domain.com/webhook"

app = Flask(__name__)
bot = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot webhook đang chạy!")

bot.add_handler(CommandHandler("start", start))

@app.route("/webhook", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot.bot)
    bot.update_queue.put(update)
    return "ok"

@app.route("/")
def home():
    return "Bot is running"

if __name__ == "__main__":
    bot.run_webhook(
        listen="0.0.0.0",
        port=5000,
        url_path="webhook",
        webhook_url=WEBHOOK_URL
    )
    app.run(host="0.0.0.0", port=5000)
