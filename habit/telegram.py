import os

import telegram

# Инициализация Telegram-бота
bot = telegram.Bot(token=os.getenv('TELEGRAM_API_TOKEN'))
