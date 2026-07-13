from telegram import Update
from telegram.ext import ContextTypes


async def anonymous_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ لینک نامعتبر است."
        )
        return

    receiver = int(context.args[0])

    context.user_data["receiver"] = receiver

    await update.message.reply_text(
        "✍️ حالا پیام ناشناس خودت را ارسال کن."
    )
