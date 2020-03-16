from auth import TOKEN
from bot import *
import logging
from telegram.ext import Updater, CommandHandler


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('saludo', saludo))
    dp.add_handler(CommandHandler('inline', inline))
    dp.add_handler(CommandHandler('latex', latex))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
