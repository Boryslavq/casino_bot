from aiogram import types

from pkg.keyboards.default.support_but import support_but
from pkg.utils.db_api.db_func import add_user
from aiogram.dispatcher import FSMContext


async def bot_start(message: types.Message):
    await message.answer("<b>Здравствуй</b>👋\n Нажми на кнопку которая тебя интересует",
                         reply_markup=await support_but())

    await add_user(message.from_user.id, message.from_user.username,
                   message.from_user.full_name)


async def close(callback: types.CallbackQuery, state: FSMContext):
    await state.reset_state()

    await callback.message.delete()
