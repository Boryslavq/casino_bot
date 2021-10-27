from aiogram import types
from pkg.data.config import CHANNEL_ID


async def reply_to_msg(message: types.Message):
    try:
        if message.sender_chat.id == CHANNEL_ID:
            await message.reply("Текст для первого коментария в канале")
    except AttributeError:
        pass
