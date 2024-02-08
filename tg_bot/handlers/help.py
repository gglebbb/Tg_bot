
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


async def bot_help(message: types.Message):
    await message.reply("Список доступных команд:\n/start\n/help\n/add_place\n/my_time")


def register_help(dp: Dispatcher):
    dp.register_message_handler(callback=bot_help, commands=["help"])
