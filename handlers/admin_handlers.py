from aiogram import Router, F
import keyboards.admin_keyboard as ak #admin keyboard
import keyboards.user_keyboard as uk #user keyboard
from aiogram.fsm.context import FSMContext
from utils.states import AddAdmin
from aiogram.types import Message
from aiogram.filters import CommandStart
from filters.is_admin import IsAdmin
from dotenv import load_dotenv
import os
load_dotenv()

ME = os.getenv('ADMIN_ME')
KATE = os.getenv('ADMIN_KATE')

admins_id = [int(ME),int(KATE)]

admin_router = Router()

#Старт бота
@admin_router.message(CommandStart(), IsAdmin(admins_id))
async def start_command(message: Message):
        await message.answer_photo(
            photo="https://avatars.dzeninfra.ru/get-zen_doc/34175/pub_5cea2361585c2f00b5c9cb0b_5cea310a752e5b00b25b9c01/scale_1200",
            reply_markup=ak.adminKeyboard)
        await message.answer(
            text=f"Привет {message.from_user.first_name} , как ты уже наверное понял(a), этот бот создан для помощи в создании кассовых документов! Если будет желание ознакомиться с gift продукций, можешь перейти в бота ниже)",
            reply_markup=uk.Start)
        await message.answer(text="У вас есть права администратора")

#Меню
@admin_router.message(F.text == "Меню", IsAdmin(admins_id))
async def menu(message: Message):
    await message.answer(text='Вы вернулись в меню!', reply_markup=ak.adminKeyboard)

#Админ-панель
@admin_router.message(F.text == "Admin-panel", IsAdmin(admins_id))
async def adminPanel(message: Message):
    await message.answer(text='Вы зашли в панель админа',reply_markup=ak.adminPanel)
#Добавление админа
@admin_router.message(F.text == "Добавить Админа")
async def admAdd(message: Message, state: FSMContext):
    await state.set_state(AddAdmin.admId)
    await message.answer(text='Введите айди нового админа(чтобы посмотреть айди, попросите написать "id" в чат бота)',
                         reply_markup=uk.MenuKeyboard)

@admin_router.message(IsAdmin(admins_id))
async def anyMess(message: Message):
    await message.answer(
        text="Вы вернулись в меню.")
    await message.answer(text='Что будем смотреть?)', reply_markup=ak.adminKeyboard)
