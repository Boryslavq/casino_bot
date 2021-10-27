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
                             callback_data=admin_callback.new(name="panel", action="send"))).add(
        InlineKeyboardButton(text="Изменить текст /start 🎺",
                             callback_data=admin_callback.new(name="panel", action="change"))

    )
    return kb


async def show_info():
    replies = {"POKERDOM": ["http://pokerdom.blefach.ru/", "POKERDOM"],
               "POKERMATCH": ["http://pokermatch.blefach.ru/", "POKERMATCH"],
               "POKERSTARS": ["http://pokerstars.blefach.ru/", "POKERSTARS"],
               "PARTYPOKER": ["http://partypoker.blefach.ru/", "PARTYPOKER"],
               "GGPOKEROK": ["http://pokerok.blefach.ru/", "GGPOKEROK"],
               "888": ["http://888poker.blefach.ru/", "888"],
               "GROMPOKER": ["https://www.grompokerru2.com/?btag=152538_l65181&AFFAGG=#?signup", "GROMPOKER"],
               }
    kb = InlineKeyboardMarkup()
    for key in replies.keys():
        kb.add(
            InlineKeyboardButton(text=replies[key][1], url=replies[key][0]))
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
