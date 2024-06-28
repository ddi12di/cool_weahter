import os
from config.config import DEFAULT_COMMANDS
from typing import List

from db.db import create_models, User

from peewee import IntegrityError

from telebot.types import BotCommand, Message
from telebot import StateMemoryStorage, TeleBot
from telebot.handler_backends import State, StatesGroup
from telebot.custom_filters import StateFilter
from search import search
from search.search import search_id
from response_api.response import Weather


class UserInfo(StatesGroup):
    name = State()
    city = State()
    сurrent_weather = State()



BOT_TOKEN = os.getenv('BOT_TOKEN')

state_storage = StateMemoryStorage()

bot = TeleBot(token=BOT_TOKEN, state_storage=state_storage)


@bot.message_handler(commands=["start"])
def handle_start(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfo.name, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username} введи свое имя')



@bot.message_handler(state=UserInfo.name)
def handle_cur_city(message: Message) -> None:
    if message.text.isalpha():

        bot.send_message(message.from_user.id,'Укажите ваш текущий город ')
        bot.set_state(message.from_user.id, UserInfo.city, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['name'] = message.text

    else:
        bot.send_message(message.from_user.id, 'Имя может содеражать толко буквы')


@bot.message_handler(state=UserInfo.city)
def get_name(message: Message) -> None:
    if message.text.isalpha():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            city_id = search_id(message.text)

            if city_id is None:
                bot.send_message(message.from_user.id, 'Попробуй еще раз, город не найден ')
            else:
                user = User.create(
                    username = message.from_user.username,
                    firstname = message.from_user.first_name,
                    city = city_id

                )
                user.save()
                data['city'] = search_id(message.text)
                text= (
                    f'Повелитель {data["name"]}\n ' \
                    f'Ваш текущий город - {Weather(city_id).city}\n' \
                    f'  На данный момент :\n'
                    f'   Температура в вашем городе - {Weather(city_id).temp}\n '\
                    f'   Ощущается температура - {Weather(city_id).feels_like}\n '\
                    f'   И для самых чувствительный-ДАВЛЕНИЕ- {Weather(city_id).pressure}\n '
                       )

                bot.send_message(message.from_user.id, text)
                bot.set_state(UserInfo.сurrent_weather, message.chat.id)
                #bot.delete_state(message.from_user.id, message.chat.id)

    else:
        bot.send_message(message.from_user.id, 'Город может содеражать толко буквы')







@bot.message_handler(state = "*", commands=['weather_current_city'])
def handle_cur_city(message: Message) -> None:
    bot.send_message(message.from_user.id,'Тут будет текущая температура в установленном городе и вывод ее ')


@bot.message_handler(state = "*", commands=['search_city'])
def handle_cur_city(message: Message) -> None:
    bot.send_message(message.from_user.id,'Поиск города и температуры !Нужно ввести город и ')





if __name__ == "__main__":
    create_models()
    bot.add_custom_filter(StateFilter(bot))
    bot.set_my_commands([BotCommand(*cmd) for cmd in DEFAULT_COMMANDS])
    bot.polling()


