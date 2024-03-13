import telebot

TOKEN = '7167269613:AAFhVjeAOyUWNVSn2SAcM9lnEJ5OpAghJ_g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот! Как могу помочь?")

bot.polling()