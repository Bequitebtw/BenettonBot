from aiogram.fsm.state import StatesGroup, State

class WriteFeedback(StatesGroup):
    feedback = State()
