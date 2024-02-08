from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message


async def bot_start(message: types.Message):
    await message.answer("Hello evrybody")
    await message.answer("<tg-spoiler> Try to type /help </tg-spoiler>")


def register_start(dp: Dispatcher):
    dp.register_message_handler(callback=bot_start, commands=["start"])
