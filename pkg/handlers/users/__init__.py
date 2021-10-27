from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart

from pkg.filters import IsGroup
from pkg.handlers.users.admin_panel import get_all, send_everyone, enter_text, panel_admin, write_id, write_text, \
    send_to_user, apply_text, change_text_panel
from pkg.handlers.users.start import bot_start, close
from pkg.keyboards.inline.inline_tasks import reply_support_callback, menu_callback, admin_callback
from pkg.handlers.users.chanells import reply_to_msg

from pkg.states import states
from pkg.data.config import ADMINS


def setup(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())

    dp.register_message_handler(panel_admin, user_id=ADMINS, commands=["admin_panel"])
    dp.register_callback_query_handler(close, text='close', state='*')

    dp.register_message_handler(IsGroup(), reply_to_msg)
    dp.register_callback_query_handler(get_all, admin_callback.filter(action="check"))
    dp.register_callback_query_handler(send_everyone, admin_callback.filter(action="advertisement"))
    dp.register_callback_query_handler(change_text_panel, admin_callback.filter(action="change"))
    dp.register_message_handler(apply_text, state=states.ChangeText.text)
    dp.register_message_handler(enter_text, state=states.AdminPanel.text)
    dp.register_callback_query_handler(write_id, admin_callback.filter(action="send"))
    dp.register_message_handler(write_text, state=states.SendMsg.id)
    dp.register_message_handler(send_to_user, state=states.SendMsg.msg)
