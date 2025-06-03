from aiogram.fsm.state import StatesGroup, State

class Elon(StatesGroup):
    phone_model = State()
    image = State()
    price = State()
    phone_number = State()
