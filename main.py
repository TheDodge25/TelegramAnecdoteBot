import telebot as tb
import token as TOKEN # Токен бота, полученный от BotFather


# Создаем экземпляр бота
bot = tb.TeleBot(TOKEN)

# Обработчик всех входящих сообщений
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, "заглушка")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(start)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(help)

# Проверка на лоха
@bot.message_handler(f=lambda message: True)
def fool_checker(message):
    if message.from_user.is_premium:
        print("Test output")

# Запускаем бота
bot.polling()