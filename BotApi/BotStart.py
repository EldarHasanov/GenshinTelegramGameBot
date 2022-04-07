import os

import telebot
from telebot import types

#import sys
#sys.path.append('../')
#import GenshinTelegramGameBot

#import sys
#sys.path.insert(0, r'/from/root/directory')
from dotenv import load_dotenv

load_dotenv()

#from ...TelegramGameBot.Secrets.Secrets import get_telegram_bot_token


bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

# Функция, обрабатывающая команду /start
# Получение сообщений от юзера

@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Roll baner")
        markup.add(item1)

        bot.send_message(m.chat.id, 'Нажми: ',  reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Roll baner':
        bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
        bot.delete_message(message.chat.id, message.message_id)
    else:
        bot.send_message(message.chat.id, 'Вы написали не то')
# Запускаем бота


bot.polling(none_stop=True, interval=0)