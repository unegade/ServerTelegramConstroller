from telebot import types
import telebot
import os
import setting

lastDir = ''

bot = telebot.TeleBot(setting.token)


@bot.message_handler(commands=['start', 'help'])
def start(msg):
    bot.send_message(msg.chat.id, "Бот еще ничего не умеет, зайдите позже.")


@bot.message_handler(commands=['getfile'])
def getfile(message):
    get_list_dir(message)


def get_list_dir(message):
    global lastDir
    if message.text == '/getfile':
        lastDir = ''
        dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        buttons = [types.KeyboardButton('%s:\\' % d) for d in dl if os.path.exists('%s:\\' % d)]
    elif message.text == '..':
        dir = os.path.dirname(lastDir)
        lastDir = dir
        buttons = os.listdir(dir)
    else:
        folder = message.text
        lastDir = os.path.join(lastDir, folder)
        buttons = os.listdir(lastDir)
        buttons.append('..')
    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(*buttons)
    bot.send_message(message.chat.id, "Выберите путь:", reply_markup=markup)
    bot.register_next_step_handler(message, get_list_dir);

print("Начало работы")
bot.polling(none_stop=True, interval=1)
