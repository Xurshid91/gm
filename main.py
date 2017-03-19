# GM Uzbekistan
"""
?
GM uchun maxsus bot ?
?
"""

import telebot
import constants

bot = telebot.TeleBot(constants.token)

# bot.send_message(287071215, "test1")

# @bot.message_handler(commands=['start'])
# def handle_text(message):
#    bot.send_message(message.chat.id, 'Salom')

# @bot.message_handler(commands=['start1'])
# def handle_text(message):
#    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('O`zbekcha', '/Русский', 'English')
    bot.send_message(message.from_user.id, 'Выберите язык', reply_markup=user_markup)

@bot.message_handler(commands=['Русский'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('Spark', 'Chevrolet', 'Cpativa')
    bot.send_message(message.from_user.id, 'Выберите авто', reply_markup=user_markup)

bot.polling(none_stop=True, interval=0)