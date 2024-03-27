from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from aiogram.types import FSInputFile
from aiogram import Router, F
from aiogram.types import Message
from apps.lists import pko_list
from apps.lists import KM3_list
from contextlib import suppress
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import WriteFeedback
from aiogram.exceptions import TelegramBadRequest
from keyboards.user_keyboard import rmk
from keyboards.user_keyboard import fb
from dotenv import load_dotenv
import os
load_dotenv()

from apps import pagination as pg

# Клавиатура пользователя
import keyboards.user_keyboard as kb

# Клавиатура админа
import keyboards.admin_keyboard as ak
from filters.is_admin import IsAdmin

ME = os.getenv('ADMIN_ME')
KATE = os.getenv('ADMIN_KATE')

admins_id = [int(ME),int(KATE)]

router = Router()

# Старт бота

# 1. Админ
@router.message(CommandStart(),IsAdmin(admins_id))
async def start_command(message: Message):
        await message.answer_photo(
            photo="https://avatars.dzeninfra.ru/get-zen_doc/34175/pub_5cea2361585c2f00b5c9cb0b_5cea310a752e5b00b25b9c01/scale_1200",
            reply_markup=kb.ReplyKeyboardDocs)
        await message.answer(
            text=f"Привет {message.from_user.first_name} , как ты уже наверное понял(a), этот бот создан для помощи в создании кассовых документов! Если будет желание ознакомиться с gift продукций, можешь перейти в бота ниже)",
            reply_markup=ak.adminKeyboard)
        await message.answer(text="У вас есть права администратора")

# 2. Пользователь
@router.message(CommandStart())
async def start_command(message: Message):
        await message.answer_photo(
            photo="https://avatars.dzeninfra.ru/get-zen_doc/34175/pub_5cea2361585c2f00b5c9cb0b_5cea310a752e5b00b25b9c01/scale_1200",reply_markup=kb.ReplyKeyboardDocs)
        await message.answer(
            text=f"Привет {message.from_user.first_name} , как ты уже наверное понял(a), этот бот создан для помощи в создании кассовых документов! Если будет желание ознакомиться с gift продукций, можешь перейти в бота ниже)",
            reply_markup=kb.Start)

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

# 1. Админ
@router.message(F.text == "Меню",IsAdmin(admins_id))
async def menu(message: Message):
    await message.answer(text='Вы вернулись в меню!', reply_markup=ak.adminKeyboard)

# 2. Пользователь
@router.message(F.text == "Меню")
async def menu(message: Message):
    await message.answer(text='Вы вернулись в меню!', reply_markup=kb.ReplyKeyboardDocs)

# Кассовая книга
@router.message(F.text == "📖 Кассовая книга")
async def kk(message: Message):
    await message.answer(text='Кассовая книга - учётный регистр, в котором отражаются в хронологическом порядке все совершенные организацией кассовые операции.')
    await message.answer_photo(photo='https://ae04.alicdn.com/kf/A01a62fb3117944e39ae9f5ce4b50c130D.png',
                               reply_markup=kb.ReplyInsideButtons)

# Возвраты
@router.message(F.text == "♻ Возвраты")
async def returns(message: Message):
    await message.answer(text='Возвраты',reply_markup=kb.ReturnsButtons)

# КМ6
@router.message(F.text == "📄 КМ6")
async def km6(message: Message):
    await message.answer(text='КМ6 - Отчет кассира за смену.',reply_markup=kb.ReplyInsideButtons)


#КМ3 /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@router.callback_query(pg.Pagination.filter(F.action.in_(["next1"])))
async def pagination_handler(call: CallbackQuery, callback_data: pg.Pagination):
    page_num = int(callback_data.page)
    page = page_num + 1
    if page_num < (len(KM3_list) - 1):
        with suppress(TelegramBadRequest):
            image = FSInputFile(KM3_list[page][0], filename="image")
            await call.message.answer_photo(photo=image)
            await call.message.answer(
                text=f"{KM3_list[page][1]}", reply_markup=pg.Km3Paginator(page))
        await call.answer()
    else:
        await call.message.answer("Вы закончили обучение!",reply_markup=kb.ReplyInsideButtons)
@router.message(F.text == "📄 КМ3")
async def km3(message: Message):
    await message.answer(text='КМ3 - Акт о возврате денежных сумм покупателям (клиентам) по неиспользованным кассовым чекам',reply_markup=kb.ReplyInsideButtons)
    image = FSInputFile(KM3_list[0][0])
    await message.answer_photo(photo=image)
    await message.answer(f"{KM3_list[0][1]}", reply_markup=pg.Km3Paginator())

# РКО ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
@router.callback_query(pg.Pagination.filter(F.action.in_(["next"])))
async def pagination_handler(call: CallbackQuery, callback_data: pg.Pagination):
    page_num = int(callback_data.page)
    page = page_num + 1
    if page_num < (len(pko_list) - 1):
        with suppress(TelegramBadRequest):
            image = FSInputFile(pko_list[page][0], filename="image")
            await call.message.answer_photo(photo=image)
            await call.message.answer(
                text=f"{page + 1}" f". " f"{pko_list[page][1]}", reply_markup=pg.PkoPaginator(page))
        await call.answer()
    else:
        await call.message.answer("Вы закончили обучение!", reply_markup=kb.ReplyInsideButtons)

@router.message(F.text == "📝 РКО")
async def rko(message: Message):
    await message.answer(text='РКО - Расходный кассовый ордер, выдача размена перед началом смены.',
                         reply_markup=kb.ReplyInsideButtons)
    image = FSInputFile(pko_list[0][0])
    await message.answer_photo(photo=image)
    await message.answer(f"1. {pko_list[0][1]}", reply_markup=pg.PkoPaginator())


# ПКО /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
    await callback.message.answer(text='Что будем смотреть?)',reply_markup=kb.ReplyKeyboardDocs)



# Админ панель
@router.message(F.text == "Admin-panel",IsAdmin(admins_id))
async def adminPanel(message: Message):
    await message.answer(text='Вы зашли в панель админа',reply_markup=ak.adminPanel)

#FEEDBACK STATE
@router.message(Command('feedback'))
async def write_feedback(message: Message, state: FSMContext):
    await state.set_state(WriteFeedback.theme)
    await message.answer(text="На какую тему хотите оставить отзыв?(Если нет подходящего варинта, напишите свой)",reply_markup=fb("Функционал"))

@router.message(WriteFeedback.theme)
async def themeFnc(message: Message, state: FSMContext):
    await state.update_data(theme=message.text)
    await state.set_state(WriteFeedback.feedback)
    await message.answer(text="Напишите о работе бота",reply_markup=kb.rmk())

@router.message(WriteFeedback.feedback)
async def fbFnc(message: Message, state: FSMContext):
    if len(message.text) < 10:
        await message.answer(text="Напиши более развернутый ответ!")
    else:
        await state.update_data(feedback=message.text)
        await message.answer(text="Спасибо за отзыв!", reply_markup=kb.ReplyInsideButtons)
        data = await state.get_data()
        await state.clear()
        formatted_text = []
        [
            formatted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]
        await message.answer_photo("https://business.yandex/wp-content/uploads/2022/07/doverie.png","\n".join(formatted_text))

# Любое сообщение от пользователя

# 1. Админ
@router.message(IsAdmin(admins_id))
async def anyMess(message: Message):
    await message.answer(
        text="Вы вернулись в меню.")
    await message.answer(text='Что будем смотреть?)',reply_markup=ak.adminKeyboard)

# 2. Пользовател
@router.message()
async def anyMess(message: Message):
    await message.answer(
        text="Вы вернулись в меню.")
    await message.answer(text='Что будем смотреть?)',reply_markup=kb.ReplyKeyboardDocs)

