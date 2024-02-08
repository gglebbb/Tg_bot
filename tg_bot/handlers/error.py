import logging

from aiogram import Dispatcher
from aiogram.types import Update
from aiogram.utils.exceptions import (TelegramAPIError,
                                      MessageNotModified,
                                      CantParseEntities)


async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param update:
    :param exception:
    :return:
    """

    if isinstance(exception, MessageNotModified):
        logging.exception("Сообщение не отредактировано")
        return True

    if isinstance(exception, CantParseEntities):
        logging.exception(f'CantParseEntities: {exception} \nUpdate: {update}')
        await Update.get_current().message.answer(f"Пoпaло в хендлер ошибок. CantParseEntities: {exception.args}")
        return True

    if isinstance(exception, TelegramAPIError):
        logging.exception(f"TelegramAPIError: {exception} \nUpdate{update}")

    logging.exception(f"Update: {update} \n{exception}")


def register_error(dp: Dispatcher):
    dp.register_message_handler(callback=errors_handler)
