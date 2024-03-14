# Импорт библиотеки telebot, которая предоставляет интерфейс для работы с API Telegram Bot
import telebot

# Ваш токен от BotFather
TOKEN = '7167269613:AAFhVjeAOyUWNVSn2SAcM9lnEJ5OpAghJ_g'

# Создание экземпляра бота с помощью токена
bot = telebot.TeleBot(TOKEN)

# Обработка команды "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Ответ на сообщение от пользователя
    bot.reply_to(message, "Привет, я бот, готов Вам помогать!!!")

# Запуск бота для постоянной обработки входящих сообщений
bot.polling()