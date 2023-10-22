import logging
from aiogram import Router, Bot, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, FSInputFile, ReplyKeyboardRemove
from aiogram.filters import Command
from bot.states import table_states
from bot.keyboars import user_keyboards
from bot.filters import user_filters
from bot.settings import PRICE_LIST, DIALOG_SCENARIO
from bot.services import calculate_price

user_router = Router()
logger = logging.getLogger(__name__)


@user_router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.clear()
    await message.answer(text=DIALOG_SCENARIO["user_answers"]["start_message"])
    await state.set_state(table_states.TableState.add_color.state)
    await message.answer(
        DIALOG_SCENARIO["user_answers"]["add_color_message"],
        reply_markup=user_keyboards.color_kb,
    )


@user_router.message(table_states.TableState.add_color, user_filters.IsColor())
async def handle_message(message: Message, state: FSMContext):
    await state.update_data(add_color=message.text.lower())
    await state.set_state(table_states.TableState.add_size.state)
    await message.answer(
        text=DIALOG_SCENARIO["user_answers"]["add_size_message"],
        reply_markup=ReplyKeyboardRemove(),
    )


@user_router.message(table_states.TableState.add_size, user_filters.IsSize())
async def handle_message(message: Message, state: FSMContext):
    await state.update_data(add_size=message.text.lower())
    await state.set_state(table_states.TableState.add_coverage.state)
    await message.answer(
        text=DIALOG_SCENARIO["user_answers"]["add_coverage_message"],
        reply_markup=user_keyboards.coverage_keyboard,
    )


@user_router.callback_query(
    table_states.TableState.add_coverage, user_filters.IsCoverage()
)
async def handle_callback(callback: CallbackQuery, state: FSMContext, answer: str):
    await state.update_data(add_coverage=answer)
    data = await state.get_data()
    await callback.message.answer(
        text=str(DIALOG_SCENARIO["user_answers"]["final_message"]).format(
            price=calculate_price(data, PRICE_LIST)
        ),
        reply_markup=ReplyKeyboardRemove(),
    )
    current_state = await state.get_state()
    if current_state:
        await state.clear()
