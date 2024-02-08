import asyncio
import logging

from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tg_bot.config import load_config
from tg_bot.handlers.time import register_time
from tg_bot.handlers.add_place import register_add_place
from tg_bot.handlers.echo import register_echo
from tg_bot.handlers.error import register_error
from tg_bot.handlers.help import register_help
from tg_bot.handlers.start import register_start

logger = logging.getLogger(__name__)


def register_all_middlewarea(dp):
    # dp.setup_middleware(...)
    pass


def register_all_filters(dp):
    # dp.filters_factory.bind(...)
    pass


def register_all_handleres(dp):
    register_start(dp)
    register_help(dp)
    register_add_place(dp)
    #register_echo(dp)
    register_time(dp)
    register_error(dp)


async def main():
    logging.basicConfig(level=logging.INFO,
                        format=u"%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s")

    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    bot['config'] = config

    await bot.send_message(chat_id=1134516906,text="Bot started to work")

    register_all_middlewarea(dp)
    register_all_filters(dp)
    register_all_handleres(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        session = await bot.get_session()
        await session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main=main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("БОТ ОСТАНОВИЛСЯ!!!!")
