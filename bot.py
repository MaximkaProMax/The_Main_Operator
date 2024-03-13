import telebot

TOKEN = '7167269613:AAFhVjeAOyUWNVSn2SAcM9lnEJ5OpAghJ_g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Коллеги, доброе утро! Ниже отметьтесь в опросе о своем фактическом выезде на работу, выбрав пункт, на котором вы сегодня работаете. Если вы вдруг опаздываете, то ниже под опросом напишите: 'Тухачевского. Опаздываю на 15 минут.'Если за час до фактического открытия пункта вы не отпишитесь, то вам автоматически будет искаться замена.")

bot.polling()