import telebot
import setting

bot = telebot.TeleBot(setting.token)


@bot.message_handler(commands=['start', 'help'])
def start(msg):
    bot.send_message(msg.chat.id, "Бот еще ничего не умеет, зайдите позже.")


print("Начало работы")
bot.polling(none_stop=True, interval=1)
