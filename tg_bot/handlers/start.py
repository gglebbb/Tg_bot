from environs import Env
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message

env = Env()
env.read_env(path=".env")


async def bot_start_with_password(message: types.Message):
    await message.answer("Hello evrybody")
    await message.answer("<tg-spoiler> Try to type /help </tg-spoiler>")


async def bot_without_password(messge: types.Message):
    await messge.answer("You don't know a password(")


def register_start(dp: Dispatcher):
    dp.register_message_handler(bot_start_with_password, CommandStart(deep_link=env.str("PASSWORD_TO_START")))
    dp.register_message_handler(bot_without_password, CommandStart())
