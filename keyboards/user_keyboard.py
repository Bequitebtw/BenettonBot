from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Клавиатура подарочных карт
GiftCardButtons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Продажа'),KeyboardButton(text='Оплата'),KeyboardButton(text='Возврат')],
    [KeyboardButton(text='Меню')],
],resize_keyboard=True)

# Клавиатура внутри пунктов
ReplyInsideButtons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Меню')]
],resize_keyboard=True)

# Клавиатура возврата
ReturnsButtons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Онлайн возврат'),KeyboardButton(text='Базовый возврат')],[KeyboardButton(text='Меню')]
],resize_keyboard=True)

# Создание клавиатуры меню
ReplyKeyboardDocs = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📖 Кассовая книга"),KeyboardButton(text="♻ Возвраты"),KeyboardButton(text="📄 КМ6")],
    [KeyboardButton(text="📄 КМ3"),KeyboardButton(text="📝 РКО"),KeyboardButton(text="📝 ПКО")],
    [KeyboardButton(text="💳 ПДК"),KeyboardButton(text="Главная")]

],resize_keyboard=True)

# MainMenu
Start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎁 Gifts',url='https://t.me/BenettonShopStoreBot')
]])

