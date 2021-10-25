from aiogram import types
from aiogram.dispatcher import FSMContext

from pkg.data import config
from pkg.keyboards.inline.inline_tasks import confirm_support, reply_support
from pkg.states import states


async def support(message: types.Message):

    await message.answer('Вы хотите обратится в поддержку?', reply_markup=await confirm_support())


async def call_support(call: types.CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer('👋 Напишите свои предложения, вопросы или проблему, с которой столкнулись\n'
                              'Мы обязательно учтём всё и примем меры 😌')
    await states.Support.add_text.set()


async def send_to_admin(message: types.Message, state: FSMContext):
    for admin in config.ADMINS:
        await message.bot.send_message(admin, '<b>↘️[MESSAGE FROM USER]↙️</b>')
        await message.copy_to(admin, reply_markup=await reply_support(message.from_user.id))
    await message.answer('Ваше сообщение успешно доставлено. Ожидайте ответ от администратора!')
    await state.finish()


async def reply_to_user(call: types.CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.edit_reply_markup()
    user_id = callback_data.get('user_id')
    await call.message.answer('Введите ответ пользователю')
    await states.Support.reply_msg.set()
    await state.update_data(user_id=user_id)


async def send_reply(message: types.Message, state: FSMContext):
    await state.update_data(reply_msg=message.text)
    async with state.proxy() as data:
        user_id = data.get('user_id')
        reply_msg = data.get('reply_msg')
    m = [
        '⚠️ У вас новое сообщение от администратора ⚠️\n',
        f'{reply_msg}'
    ]
    await message.bot.send_message(user_id, '\n'.join(m))
    await state.finish()
