from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import CommandStart

from pkg.handlers.users.admin_panel import get_all, send_everyone, enter_text, panel_admin, write_id, write_text, \
    send_to_user
from pkg.handlers.users.start import bot_start, close
from pkg.handlers.users.support import call_support, support, send_to_admin, reply_to_user, send_reply
from pkg.handlers.users.handler import show_link, poker_show, back
from pkg.keyboards.inline.inline_tasks import reply_support_callback, menu_callback, admin_callback

from pkg.states import states
from pkg.data.config import ADMINS
from pkg.utils.misc import rate_limit


def setup(dp: Dispatcher, ):
    dp.register_message_handler(bot_start, CommandStart())

    dp.register_message_handler(panel_admin, user_id=ADMINS, commands=["admin_panel"])
    dp.register_callback_query_handler(close, text='close', state='*')

    dp.register_callback_query_handler(get_all, admin_callback.filter(action="check"))
    dp.register_callback_query_handler(send_everyone, admin_callback.filter(action="advertisement"))
    dp.register_message_handler(enter_text, state=states.AdminPanel.text)
    dp.register_callback_query_handler(write_id, admin_callback.filter(action="send"))
    dp.register_message_handler(write_text, state=states.SendMsg.id)
    dp.register_message_handler(send_to_user, state=states.SendMsg.msg)

    dp.register_message_handler(show_link, text="Ссылки 🌝")
    dp.register_message_handler(support, text='Обратная связь 📲')

    dp.register_callback_query_handler(poker_show, menu_callback.filter())
    dp.register_callback_query_handler(back, text='back')

    dp.register_callback_query_handler(call_support, text='confirm')
    dp.register_message_handler(send_to_admin, state=states.Support.add_text, content_types=types.ContentType.ANY)
    dp.register_callback_query_handler(reply_to_user, reply_support_callback.filter(name='reply'))
    dp.register_message_handler(send_reply, state=states.Support.reply_msg)
