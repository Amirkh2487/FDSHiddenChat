from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import TOKEN
from database import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    add_user(user.id)

    await update.message.reply_text(
        "👋 به FDSHiddenChat خوش اومدی."
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
