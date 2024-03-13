import telebot

TOKEN = '7167269613:AAFhVjeAOyUWNVSn2SAcM9lnEJ5OpAghJ_g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        bot.send_message(message.chat.id, "Коллеги, доброе утро! Ниже отметьтесь в опросе о своем фактическом выезде на работу, выбрав пункт, на котором вы сегодня работаете. Если вы вдруг опаздываете, то ниже под опросом напишите: 'Тухачевского. Опаздываю на 15 минут.'Если за час до фактического открытия пункта вы не отпишитесь, то вам автоматически будет искаться замена.")
        bot.send_poll(message.chat.id, "Когда вы прибыли на работу?", ["Полежаевская - 09:00", "Соколовского - 09:00", "Аэропорт - 09:00", "Черняховского - 09:00", "Карбышева 16 OZON - 09:00", "Строгино - 09:00", "Басманная - 09:00", "Зеленоградская - 09:00", "Тухачевского 22к3 - 09:00", "Посмотреть результаты"], is_anonymous=False)
        bot.send_poll(message.chat.id, "Когда вы прибыли на работу?", ["Карбышева 16 WB - 09:00", "Тухачевского 50 - 09:00", "Фили Ozon - 09:00", "Фили WB - 09:00", "Ясенево ЯМ - 09:00", "Воротынская - 09:00", "Яна Райниса - 09:00", "Посмотреть результаты"], is_anonymous=False)
        bot.send_poll(message.chat.id, "Когда вы прибыли на работу?", ["Фомичёвой OZON - 09:00", "Фомичёвой WB - 09:00", "Фомичёвой YM - 9:00", "Аминьевская - 9:00", "Беловежская YM - 10:00", "Карбышева &c3 OZON - 09:00", "Карбышева &c3 YM - 09:00", "Левченко YM - 9:00", "Левченко OZON - 9:00", "Посмотреть результаты"], is_anonymous=False)
    except telebot.apihelper.ApiTelegramException as e:
        if e.result.status_code == 400 and 'message to reply not found' in e.result.text:
            print("Сообщение для ответа не найдено")
        else:
            raise e

bot.polling()
