from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

# Пагинаторы
class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int

def PkoPaginator(page: int=0,):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➡️", callback_data=Pagination(action="next", page=page).pack()))
    return builder.as_markup()

def Km3Paginator(page: int=0):
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➡️", callback_data=Pagination(action="next1", page=page).pack()))
    return builder.as_markup()
def PcoPaginator(page: int=0): #ПКО
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➡️", callback_data=Pagination(action="next2", page=page).pack()))
    return builder.as_markup()