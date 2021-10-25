from typing import Union

from aiogram import types
from pkg.keyboards.inline.inline_tasks import menu, show_info


async def show_link(message: Union[types.Message, types.CallbackQuery]):
    msg = "Какая ссылка тебе нравиться?"
    if isinstance(message, types.CallbackQuery):
        call = message
        await call.message.edit_text(msg, reply_markup=await menu())
    if isinstance(message, types.Message):
        await message.answer(msg, reply_markup=await menu())


async def poker_show(callback: types.CallbackQuery, callback_data: dict):
    key = callback_data.get("outline")
    text = {"dom": "Text1",
            "match": "Text2",
            "starts": "Text3",
            "party": "Text4",
            "gg": "Text5",
            "888": "Text6",
            "best": "Text7",
            }
    await callback.message.edit_text(text[key], reply_markup=await show_info(key))


async def back(callback: types.CallbackQuery):
    await show_link(callback)
