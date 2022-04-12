import os
import random

import telebot
from telebot import types
import sqlalchemy as sq


#import sys
#sys.path.append('../')
#import DatabaseConnectClass as DB



import sys
sys.path.insert(0, 'C:\PythonProjects\Genshin\IntrestingStuff\TelegramGameBot\DataBase')
from dotenv import load_dotenv
import DatabaseConnectClass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

load_dotenv()

#from ...TelegramGameBot.Secrets.Secrets import get_telegram_bot_token

Base = declarative_base()
bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"))

engine = sq.create_engine(os.getenv("SQL_DATA_BASE"), echo=False)
Base.metadata.create_all(engine)


# Функция, обрабатывающая команду /start
# Получение сообщений от юзера

@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Get my element")
        markup.add(item1)

        bot.send_message(m.chat.id, 'Нажми: ',  reply_markup=markup)
        s = Session(engine)
        q = s.query(DatabaseConnectClass.Elements)
        num = q.count()
        print(num)
        print(q[num - 1].beauty_name)
        for a_rec in q:
            print(a_rec.beauty_name)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'Get my element':
        bot.delete_message(message.chat.id, message.message_id)
        s = Session(engine)
        q = s.query(DatabaseConnectClass.TelegramUser).get(message.chat.id)

        if q == None:
            elemets_q = s.query(DatabaseConnectClass.Elements)
            num = elemets_q.count()
            numOfEl = random.randint(0, num-1)
            s.add(DatabaseConnectClass.TelegramUser(usr_name=message.chat.id, element=elemets_q[numOfEl].name))
            #sq.insert(DatabaseConnectClass.TelegramUser)
        else:
            bot.send_message(message.chat.id, ('Your element: ' + s.query(DatabaseConnectClass.Elements).get(q.element).beauty_name))
        s.commit()

    else:
        bot.send_message(message.chat.id, 'Ви помилились з командою')
# Запускаем бота


bot.polling(none_stop=True, interval=0)