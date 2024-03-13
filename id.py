# Импортируем библиотеку requests для выполнения HTTP-запросов
import requests

# Ваш токен от BotFather
TOKEN = '7167269613:AAFhVjeAOyUWNVSn2SAcM9lnEJ5OpAghJ_g'

# Выполняем GET-запрос к API Telegram, чтобы получить обновления
response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')

# Преобразуем ответ от API в JSON-формат
updates = response.json()

# Проходимся по всем обновлениям
for update in updates['result']:
    # Проверяем, есть ли ключ 'message' в обновлении
    if 'message' in update:
        # Получаем ID чата из каждого обновления
        chat_id = update['message']['chat']['id']

        # Выводим ID чата
        print(chat_id)