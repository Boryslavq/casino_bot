from asyncio import sleep
import csv
from aiogram import types
from aiogram.dispatcher import FSMContext

from pkg.keyboards.inline.inline_tasks import cancel_kb, panel
from pkg.states.states import AdminPanel, SendMsg, ChangeText
from pkg.utils.db_api.db_func import get_count_users, get_all_users
from pkg.data.config import GROUP_CHAT_ID


async def panel_admin(message: types.Message):
    await message.answer("Выберите действие", reply_markup=await panel())


async def get_all(callback: types.CallbackQuery):
    count = await get_count_users()
    users = await get_all_users()
    fied_names = ["user_id", "username", "fullname"]
    with open("new.csv", "w", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fied_names)
        writer.writeheader()

    for user in users:
        with open("new.csv", "a", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow((user.user_id, user.username, user.fullname,))

    await callback.bot.send_document(caption=f"Общее количество пользователей: {count}",
                                     chat_id=callback.message.chat.id,
                                     document=open("new.csv", "rb"))


async def send_everyone(callback: types.CallbackQuery):
    await callback.message.edit_text("Пришлите текст рассылки", reply_markup=await cancel_kb())
    await AdminPanel.text.set()


async def enter_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    text = message.text
    users = await get_all_users()
    for user in users:
        try:
            await message.bot.send_message(chat_id=user.user_id, text=text)
            await sleep(0.3)
        except Exception:
            pass
    await message.bot.send_message(chat_id=GROUP_CHAT_ID, text=text)
    await message.answer("Рассылка окончена")
    await state.finish()


async def write_id(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите ID пользователя", reply_markup=await cancel_kb())
    await SendMsg.id.set()


async def write_text(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    await message.answer("Введите текст...")
    await SendMsg.msg.set()


async def send_to_user(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    text = data.get("text")
    ID = data.get("id")
    msg = [
        '⚠️ У вас новое сообщение от администратора ⚠️\n',
        f'{text}'
    ]

    try:
        await message.bot.send_message(chat_id=ID, text="\n".join(msg))
        await message.answer("Сообщение отправлено!")
    except Exception:
        await message.answer("ID не был найден")
    await state.finish()


async def change_text_panel(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите текст... ", reply_markup=await cancel_kb())
    await ChangeText.text.set()


async def apply_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    text = message.text
    await state.finish()

    with open("new.txt", "w", encoding="utf-8") as file:
        file.write(text)

    await message.answer("Сообщение успешно изменено")
