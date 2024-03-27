from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.states import WriteFeedback, AddAdmin
from keyboards import user_keyboard as uk
from keyboards import admin_keyboard as ak
from filters.is_admin import IsAdmin
feedback_router = Router()
from dotenv import load_dotenv
import os
load_dotenv()

ME = os.getenv('ADMIN_ME')
KATE = os.getenv('ADMIN_KATE')

admins_id = [int(ME),int(KATE)]

@feedback_router.message(WriteFeedback.theme)
async def themeFnc(message: Message, state: FSMContext):
    if message.text == "Меню":
        await state.clear()
        await message.answer(text='Вы вернулись в меню!', reply_markup=uk.MainButtons)
    else:
        await state.update_data(theme=message.text)
        await state.set_state(WriteFeedback.feedback)
        await message.answer(text="Напишите о работе бота", reply_markup=uk.MenuKeyboard)

@feedback_router.message(WriteFeedback.feedback)
async def fbFnc(message: Message, state: FSMContext):
    if message.text == "Меню":
        await state.clear()
        await message.answer(text='Вы вернулись в меню!', reply_markup=uk.MainButtons)
    if len(message.text) < 1:
        await message.answer(text="Напиши более развернутый ответ!")
    else:
        await state.update_data(feedback=message.text)
        data = await state.get_data()
        await state.clear()
        formatted_text = []
        form = []
        for value in data.items():
            form.append(value)
        [
            formatted_text.append(f"{key}: {value}")
            for key, value in data.items()
        ]
        await message.answer_photo("https://business.yandex/wp-content/uploads/2022/07/doverie.png","\n".join(formatted_text))
        await message.answer(text="Спасибо за отзыв!", reply_markup=uk.MenuKeyboard)
        await message.forward(-1002124575016)

#Добавление админа
@feedback_router.message(AddAdmin.admId,IsAdmin(admins_id))
async def addAdm(message: Message, state: FSMContext):
    if message.text == "Меню":
        await state.clear()
        await message.answer(text='Вы вернулись в меню!', reply_markup=uk.MainButtons)
    if message.text.isdigit() and len(message.text) == 9:
        await state.update_data(id=int(message.text))
        await state.set_state(AddAdmin.admId)
        await message.answer(text='Новый админ добавлен!',reply_markup=ak.adminKeyboard)
        await state.clear()
    elif message.text == "id":
        await message.answer(f'Это ваш айди: {message.from_user.id}.Нужен того, кого вы добавляете)')
    else:
        await message.answer(text='Айди должно составлять 9 цифр(чтобы посмотреть айди, попросите написать "id" в чат бота)')