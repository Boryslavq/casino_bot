from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode

from pkg.utils.db_api import database
from pkg.utils.db_api.database import db

from pkg.data import config


async def on_startup(dispatcher: Dispatcher):
    from pkg import middlewares
    from pkg import filters
    from pkg import handlers

    middlewares.setup(dp)
    filters.setup(dp)
    handlers.users.setup(dp)
    handlers.errors.setup(dp)

    await database.on_startup(dp)
    await db.gino.create_all()
    # await db.gino.drop_all()


if __name__ == '__main__':
    bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, validate_token=True)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)

    executor.start_polling(dp, on_startup=on_startup)
