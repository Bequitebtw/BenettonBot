from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import WriteFeedback
import keyboards.user_keyboard as kb

router = Router()

@router.message(Command('feedback'))
async def write_feedback(message: Message, state: FSMContext):
    await message.answer('Напишите отзыв по поводу бота)')


async def feedback(message: Message):
    await message.forward(chat_id=804555908, text=message.text)
    await message.answer('Cпасибо за оставленный отзыв!',reply_markup=kb.ReplyInsideButtons)