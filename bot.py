from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_NEW_TOKEN_HERE"   # <-- Yaha BotFather se naya token daalna

async def girl_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user.first_name
    msg = update.message.text.lower()

    if "hi" in msg or "hello" in msg:
        reply = f"Hii {user} 😘 kya kar rahe ho?"
    elif "kya kar rahi" in msg:
        reply = "Bas tumhari yaad aa rahi thi 😌"
    elif "love" in msg:
        reply = "Hehe 😳 tum to flirty ho gaye…"
    elif "miss" in msg:
        reply = "Sach me? ❤️ Kitna miss kiya mujhe?"
    else:
        reply = "Acha… aur batao sweetie 😄"

    await update.message.reply_text(reply)


app = ApplicationBuilder().token(8306688208:AAGSSOr3Y5PEnB8HlV-xRbK7yLt0kjd3774).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, girl_chat))
app.run_polling()
