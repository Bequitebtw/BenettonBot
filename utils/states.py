from aiogram.fsm.state import StatesGroup, State

class WriteFeedback(StatesGroup):
    theme = State()
    feedback = State()

class AddAdmin(StatesGroup):
    admId = State()