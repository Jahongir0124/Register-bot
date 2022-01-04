import telebot
from var import *
from telebot import types
bot = telebot.TeleBot('2083349158:AAFBycF-ilcRN4tGjbFtDRoTGIqlD9DN6r8')
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(advert) for advert in button])
    bot.send_message(message.chat.id, "😊Assalomu aleykum!\n🍀LaminaLife kompaniyasining rasmiy botiga xush kelibsiz!",reply_markup=markup)
@bot.message_handler(content_types='text')
def restart(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    item = types.KeyboardButton("Telefon nomer jo'natish",request_contact=True)
    keyboard.add(item)
    bot.send_message(message.chat.id,otvet[message.text])
    response = bot.send_message(message.chat.id,answer,reply_markup=keyboard)
    bot.register_next_step_handler(response, begin)
@bot.message_handler(commands=['restart'])
def begin(message):
    markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=True)
    markup.add(*[types.KeyboardButton(advert) for advert in button])
    bot.send_message(message.chat.id, "Marhamat sizga kerakli bo'imni tanlang!",reply_markup=markup)
bot.infinity_polling()