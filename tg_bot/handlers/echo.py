from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode

async def bot_echo_all(message: types.Message, state: FSMContext, ):
    if message.text == "Glebbb19":
        await message.answer("...")
        print("Easter egg!!!!!!")
    if message.text == "delete":
        await message.answer("  ")
    else:
        await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(bot_echo_all, state='*', content_types=types.ContentType.ANY)
