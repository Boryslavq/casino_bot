from datetime import datetime
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

menu_callback = CallbackData('menu', 'name', 'outline')
reply_support_callback = CallbackData('support', 'name', 'user_id')
admin_callback = CallbackData("admin", "name", "action")


async def panel():
    kb = InlineKeyboardMarkup()

    kb.add(InlineKeyboardButton(text="Посмотреть всех пользователей 📣",
                                callback_data=admin_callback.new(name="panel", action="check"))).add(
        InlineKeyboardButton(text="Разослать рассылку 🎬",
                             callback_data=admin_callback.new(name="panel", action="advertisement"))).add(
        InlineKeyboardButton(text="Отправить сообщение конкретному пользователю 💫",
                             callback_data=admin_callback.new(name="panel", action="send"))

    )
    return kb


async def show_info(key: str):
    replies = {"dom": ["https://www.instagram.com/?hl=ru", "Text1"],
               "match": ["https://www.instagram.com/?hl=ru", "Text2"],
               "starts": ["https://www.instagram.com/?hl=ru", "Text3"],
               "party": ["https://www.instagram.com/?hl=ru", "Text4"],
               "gg": ["https://www.instagram.com/?hl=ru", "Text5"],
               "888": ["https://www.instagram.com/?hl=ru", "Text6"],
               "best": ["https://www.instagram.com/?hl=ru", "Text7"],
               }
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text=replies[key][1], url=replies[key][0])).add(
        InlineKeyboardButton(text="Назад", callback_data='back')
    )
    return kb


async def menu() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='PokerDom', callback_data=menu_callback.new(name='poker', outline='dom'))).add(
        InlineKeyboardButton(text='PokerMatch', callback_data=menu_callback.new(name='poker', outline='match'))).add(
        InlineKeyboardButton(text='PokerStars', callback_data=menu_callback.new(name='poker', outline='starts'))).add(
        InlineKeyboardButton(text='PartyPoker', callback_data=menu_callback.new(name='poker', outline='party'))).add(
        InlineKeyboardButton(text='GGpokerok', callback_data=menu_callback.new(name='poker', outline='gg'))).add(
        InlineKeyboardButton(text='888Poker', callback_data=menu_callback.new(name='poker', outline='888'))).add(
        InlineKeyboardButton(text='BestPoker', callback_data=menu_callback.new(name='poker', outline='best')))
    return kb


async def confirm_support() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Да', callback_data='confirm'),
           InlineKeyboardButton(text='Нет', callback_data='close'))
    return kb


async def reply_support(user_id: int) -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Ответить', callback_data=reply_support_callback.new(name='reply',
                                                                                          user_id=user_id)),
           InlineKeyboardButton(text='Игнорировать', callback_data='close'))
    return kb


async def cancel_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(text='Отмена', callback_data='close'))
    return kb
