from aiogram.fsm.state import StatesGroup, State


class TableState(StatesGroup):
    add_color = State()
    add_size = State()
    add_coverage = State()
