from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot import settings


class IsColor(BaseFilter):
    async def __call__(self, message: Message = None) -> bool:
        if message.text in settings.PRICE_LIST["color"].keys():
            return True
        else:
            await message.answer(
                text=settings.DIALOG_SCENARIO["user_answers"]["add_color_error"]
            )


class IsSize(BaseFilter):
    async def __call__(self, message: Message = None) -> bool:
        if message.text in settings.PRICE_LIST["size"].keys():
            return True
        else:
            await message.answer(
                text=settings.DIALOG_SCENARIO["user_answers"]["add_size_error"]
            )


class IsCoverage(BaseFilter):
    async def __call__(
        self, callback: CallbackQuery = None, message: Message = None
    ) -> bool:
        if callback.data == "yes":
            return {"answer": "да"}
        elif callback.data == "no":
            return {"answer": "нет"}
        elif message:
            await callback.message.answer(
                text=settings.DIALOG_SCENARIO["user_answers"]["add_coverage_error"]
            )
            return False
