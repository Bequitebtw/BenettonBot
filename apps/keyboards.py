from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# DocsMenu массив
DocsMenu = ["📖 Кассовая книга","♻ Возвраты","📄 КМ6","📄 КМ3","📝 РКО","📝 ПКО","💳 ПДК","Главная"]

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

async def ReplyKeyboardDocs():
    keyboard = ReplyKeyboardBuilder()
    for doc in DocsMenu:
        keyboard.add(KeyboardButton(text=doc))
    return keyboard.adjust(3,2).as_markup()

# Клавиатура внутри пунктов()
InlineInsideButtons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Далее ->',callback_data='next')],
    [InlineKeyboardButton(text='<- Назад',callback_data='back')]
])

# MainMenu
Start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎁 Gifts',url='https://t.me/BenettonShopStoreBot')
        # ,InlineKeyboardButton(text='📇 Documents',callback_data='docs')],
]])
