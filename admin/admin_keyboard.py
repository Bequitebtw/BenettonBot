from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

admin = ["📖 Кассовая книга","♻ Возвраты","📄 КМ6","📄 КМ3","📝 РКО","📝 ПКО","💳 ПДК","Главная"]
adminPanel = ["Рассылка","Добавить Админа","Меню"]


async def adminKeyboard():
    keyboard = ReplyKeyboardBuilder()
    for doc in admin:
        keyboard.add(KeyboardButton(text=doc))
    return keyboard.adjust(3,2).as_markup()

async def adminPanelKeyboard():
    keyboard = ReplyKeyboardBuilder()
    for doc in adminPanel:
        keyboard.add(KeyboardButton(text=doc))
    return keyboard.adjust(1,1).as_markup()