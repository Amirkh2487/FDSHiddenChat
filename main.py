from telegram.ext import (
    Application,
    CommandHandler,
)

from config import TOKEN
from handlers.start import start
from handlers.message import anonymous_message


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("msg", anonymous_message))

    print("FDSHiddenChat Started...")
    app.run_polling()


if __name__ == "__main__":
    main()
