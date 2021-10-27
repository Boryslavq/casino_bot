from aiogram import Dispatcher

from .is_admin import AdminFilter
from .is_group import IsGroup


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsGroup)