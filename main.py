from auth import TOKEN
from bot import *
from telegram.ext import Updater, CommandHandler


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    # comandos admitidos
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('saludo', saludo))
    dp.add_handler(CommandHandler('inline', inline))
    dp.add_handler(CommandHandler('latex', latex))

    # error logging
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
