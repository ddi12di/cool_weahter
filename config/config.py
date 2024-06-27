import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загруженrы т.к отсутствует файл .env")
else:

    load_dotenv()



DEFAULT_COMMANDS = (
    ("start", "Начать работу"),
    ("current_city", "Указать текущий город"),
    ("weather_current_city", "Температура в моем городе"),
    ("search_city", "Поиск города и показ температуры")
)

