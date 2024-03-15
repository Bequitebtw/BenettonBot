from aiogram import F, Router
from aiogram.filters import CommandStart,Command
from aiogram.types import Message, CallbackQuery

# Клавиатура пользователя
import apps.keyboards as kb

# Клавиатура админа
import admin.admin_keyboard as ak

admins_id = ['804555908','856935419']
router = Router()

# Старт бота
@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer_photo(
        photo="https://avatars.dzeninfra.ru/get-zen_doc/34175/pub_5cea2361585c2f00b5c9cb0b_5cea310a752e5b00b25b9c01/scale_1200",reply_markup=await kb.ReplyKeyboardDocs())
    await message.answer(
        text=f"Привет {message.from_user.first_name} , как ты уже наверное понял(a), этот бот создан для помощи в создании кассовых документов!",
        reply_markup=kb.Start)

# Кнопка назад
@router.message(F.text == "<- Назад")
async def back(message: Message):
    await message.answer(text='Что будем смотреть?)', reply_markup=await kb.ReplyKeyboardDocs())

# Главная
@router.message(F.text == "Главная")
async def main(message: Message):
    await message.answer(
        text="Вы вернулись в меню.")
    await message.answer_photo(
        photo="https://avatars.dzeninfra.ru/get-zen_doc/34175/pub_5cea2361585c2f00b5c9cb0b_5cea310a752e5b00b25b9c01/scale_1200",reply_markup=kb.Start)

#userId
@router.message(F.text == "id")
async def id(message: Message):
    await message.answer(f'{message.from_user.id}')

# Меню
@router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer(text='Что будем смотреть?)', reply_markup=await kb.ReplyKeyboardDocs())

# Кассовая книга
@router.message(F.text == "📖 Кассовая книга")
async def kk(message: Message):
    await message.answer_photo(photo='https://ae04.alicdn.com/kf/A01a62fb3117944e39ae9f5ce4b50c130D.png',reply_markup=kb.ReplyInsideButtons)
    await message.answer(text='Кассовая книга - учётный регистр, в котором отражаются в хронологическом порядке все совершенные организацией кассовые операции.',reply_markup=kb.InlineInsideButtons)


# Возвраты
@router.message(F.text == "♻ Возвраты")
async def returns(message: Message):
    await message.answer(text='Возвраты',reply_markup=kb.ReturnsButtons)

# КМ6
@router.message(F.text == "📄 КМ6")
async def km6(message: Message):
    await message.answer(text='КМ6 - Отчет кассира за смену.',reply_markup=kb.ReplyInsideButtons)

# КМ3
@router.message(F.text == "📄 КМ3")
async def km3(message: Message):
    await message.answer(text='КМ3 - Акт о возврате денежных сумм покупателям (клиентам) по неиспользованным кассовым чекам',reply_markup=kb.ReplyInsideButtons)

# РКО
@router.message(F.text == "📝 РКО")
async def rko(message: Message):
    await message.answer(text='РКО - Расходный кассовый ордер, выдача размена перед началом смены.',reply_markup=kb.ReplyInsideButtons)

# ПКО
@router.message(F.text == "📝 ПКО")
async def pko(message: Message):
    await message.answer(text='ПКО - Приходный кассовый ордер, возврат размена + выручки после смены.',reply_markup=kb.ReplyInsideButtons)

# ПДК
@router.message(F.text == "💳 ПДК")
async def pdk(message: Message):
    await message.answer(text='ПДК - Подарочная карта',reply_markup=kb.GiftCardButtons)

# Документы
@router.callback_query(F.data == 'docs')
async def docs(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.answer(text='Что будем смотреть?)',reply_markup=await kb.ReplyKeyboardDocs())

# Админ панель
@router.message(Command("admin"))
async def adminPanel(message: Message):
    for id in admins_id:
        if(int(id) == message.from_user.id):
            await message.answer(text='Вы зашли в панель админа',reply_markup=await ak.adminPanelKeyboard())


# Любое сообщение от пользователя + вкладка для admin
@router.message()
async def anyMess(message: Message):
    await message.answer(
        text="Вы вернулись в меню.")
    await message.answer(text='Что будем смотреть?)')
