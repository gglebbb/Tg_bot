import asyncio
from aiogram import types, Dispatcher
from tg_bot.handlers import places
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


async def bot_add_place(message: types.Message):
    await add_country(message)
    await add_city(message)


async def add_country(message: types.Message):
    await message.answer("Type country:")
    await helper_for_country(message)
    country = places.country_dop
    if " " in country:
        country.replace(" ", "+")
    await message.answer("Country has been added")
    places.countries = country
    places.country_dop = ""


async def add_city(message: types.Message):
    await message.answer("Type city:")
    await helper_for_city(message)
    city = places.city_dop
    if " " in city:
        city.replace(" ", "+")
    await message.answer("City added")
    places.cities = city
    places.city_dop = ""


async def helper_for_country(message: types.Message):
    places.country_dop = message.text


async def helper_for_city(message: types.Message):
    places.city_dop = message.text

def register_add_place(dp: Dispatcher):
    dp.register_message_handler(callback=bot_add_place, commands=["add_place"])
