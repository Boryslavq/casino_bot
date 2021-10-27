from aiogram import Dispatcher
from aiogram.utils.executor import Executor
from gino import Gino
from sqlalchemy import Column

from pkg.data import config

db = Gino()


class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer(), unique=True)
    username = db.Column(db.Unicode())
    fullname = db.Column(db.Unicode())
    created_at = Column(db.DateTime(True), server_default=db.func.now())
    updated_at = Column(db.DateTime(True),
                        default=db.func.now(),
                        onupdate=db.func.now(),
                        server_default=db.func.now(), )


async def on_startup(dispatcher: Dispatcher):
    await db.set_bind(config.POSTGRES_URI)


def setup(executor: Executor):
    executor.on_startup(on_startup)
