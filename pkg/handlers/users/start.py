from aiogram import types

from pkg.keyboards.inline.inline_tasks import show_info
from pkg.utils.db_api.db_func import add_user
from aiogram.dispatcher import FSMContext


async def bot_start(message: types.Message):
    with open("new.txt", "r", encoding="utf-8") as f:
        text = f.read()

    await message.answer(text,
                         reply_markup=await show_info())

    await add_user(message.from_user.id, message.from_user.username,
                   message.from_user.full_name)


async def close(callback: types.CallbackQuery, state: FSMContext):
    await state.reset_state()

    await callback.message.delete()
