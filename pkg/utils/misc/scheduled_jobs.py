from datetime import datetime

from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from utils.db_api import db_func as db
from localization import _


async def start_new_day():
    today = datetime.today().weekday()
    users = await db.get_users()
    for user_id in users:
        tasks = await db.get_tasks(user_id[0], today - 1)
        for task in tasks:
            if not task[2]:
                await db.add_task(user_id[0], task[1], today)
            await db.delete_task(task[0])


async def send_morning_notif(dp: Dispatcher):
    today = datetime.today().weekday()
    for user in await db.get_users_notif():
        tasks = await db.get_tasks(user[0], today)
        if len(tasks) != 0:
            m = _('👋 Доброе утро. Новый день - новые возможности!'
                  ' Следуйте своему плану и не забывайте добавлять задачи,'
                  ' чтобы повысить свою продуктивность!'
                  ' Хорошего дня и удачи 🌟')
            await dp.bot.send_message(user[0], m)
        else:
            m = _('👋 Доброе утро. Новый день - новые возможности! Вы ещё не '
                  'добавили задач на сегодня 🙁, сделайте это, чтобы повысить '
                  'продуктивность! Хорошего дня и удачи 🌟')
            await dp.bot.send_message(user[0], m)


async def send_evening_notif(dp: Dispatcher):
    for user in await db.get_users_notif():
        m = _('👋 День подходит к концу. Не забудьте выставить цели на завтра! '
              'Удачи в достижении твоей цели, каждый шаг - это успех 🌟')
    await dp.bot.send_message(user[0], m)


def setup(scheduler: AsyncIOScheduler, dp: Dispatcher):
    scheduler.add_job(start_new_day, 'cron', hour=0)  # Transferring tasks from yesterday to today
    scheduler.add_job(send_morning_notif, 'cron', hour=9, args=[dp])  # Sending morning reminder
    scheduler.add_job(send_evening_notif, 'cron', hour=22, args=[dp])  # Sending evening reminder

    scheduler.start()
