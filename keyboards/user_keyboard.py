from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove

rmk = ReplyKeyboardRemove

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
    [KeyboardButton(text="💳 ПДК"),KeyboardButton(text="Главная"),KeyboardButton(text="Оставить отзыв")]

],resize_keyboard=True)

# MainMenu
Start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎁 Gifts',url='https://t.me/BenettonShopStoreBot')
]])

def fb(text: str| list):
    builder = ReplyKeyboardBuilder()
    builder.adjust(2,2)
    if isinstance(text, str):
        text = [text]
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True,one_time_keyboard=True)