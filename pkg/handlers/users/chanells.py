from aiogram import types
from pkg.data.config import CHANNEL_ID


async def reply_to_msg(message: types.Message):
    try:
        if message.sender_chat.id == CHANNEL_ID:
            await message.reply(
                "🤞Обсудить новость, блеснуть остроумием, получить билеты от модератора и тп можно в нашем чатике 👉 @BlefachChat\n🍀 Хочешь играть наши приватные турниры? Пиши мне @blefach_linksbot")
    except AttributeError:
        pass
