from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def support_but():
    keyboard = [
        [
            KeyboardButton(text="Ссылки 🌝"),
            KeyboardButton(text="Обратная связь 📲")

        ],
    ]
    kb = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    return kb
