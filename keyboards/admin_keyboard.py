from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


adminPanel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Рассылка"),KeyboardButton(text="Добавить Админа")],
    [KeyboardButton(text="Меню"),]

],resize_keyboard=True)

adminKeyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📖 Кассовая книга"),KeyboardButton(text="♻ Возвраты"),KeyboardButton(text="📄 КМ6")],
    [KeyboardButton(text="📄 КМ3"),KeyboardButton(text="📝 РКО"),KeyboardButton(text="📝 ПКО")],
    [KeyboardButton(text="💳 ПДК"),KeyboardButton(text="Главная"),KeyboardButton(text="Admin-panel")]

],resize_keyboard=True)