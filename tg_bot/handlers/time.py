from aiogram import types, Dispatcher
from tg_bot.handlers import places
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as BS
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode


async def bot_time(message: types.Message, state: FSMContext, ):
    if len(places.cities) != 0:
        print(f"Time in {places.cities[0]},{places.countries[0]}:{time_finder(places.cities[0], places.countries[0])}")
        await message.answer(
            f"Time in {places.cities[0]},{places.countries[0]}:{time_finder(places.cities[0], places.countries[0])}"
        )
    else:
        await message.answer("No places at your list")


def time_finder(city, country):
    if " " in city:
        city = city.replace(" ", "+")
    if " " in country:
        country = country.replace(" ", "+")
    s = ""
    res = ""
    lst = []
    url = f"https://www/google.com/search&q={city}+{country}+what+time?+&start"
    letters = "qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю,"

    session = HTMLSession()
    r = session.get(url)

    html = BS(r.content, "lxml")
    lst += html.text.split(" ")
    for i in range(len(lst)):
        if "время" in lst[i] and ":" in lst[i]:
            s += lst[i]
    prom = list(s)
    for i in range(len(prom)):
        if not (prom[i] in letters):
            res += prom[i]
    return res


def register_time(dp: Dispatcher):
    dp.register_message_handler(callback=bot_time, commands=["my_time"])
