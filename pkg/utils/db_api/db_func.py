import logging

from asyncpg import UniqueViolationError

from pkg.utils.db_api.database import User, db


async def get_count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def get_all_users():
    all_users = await User.query.gino.all()
    return all_users


async def add_user(user_id: int, username: str, full_name: str):
    try:
        await User.create(user_id=user_id, username=username,
                          fullname=full_name)
    except UniqueViolationError:
        await User.update.values(username=username, fullname=full_name).where(
            'user_id' == user_id).gino.status()
