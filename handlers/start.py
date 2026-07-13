from telegram import Update
from telegram.ext import ContextTypes

from database import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(user.id)

    bot = await context.bot.get_me()

    link = f"https://t.me/{bot.username}?start={user.id}"

    await update.message.reply_text(
        f"""👋 سلام {user.first_name}

🔗 لینک ناشناس تو:

{link}

این لینک را برای دوستانت بفرست تا ناشناس برایت پیام ارسال کنند.
"""
    )
