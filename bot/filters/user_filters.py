from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from bot import settings


class IsColor(BaseFilter):
    async def __call__(self, message: Message = None) -> bool:
        if message.text in settings.PRICE_LIST["color"].keys():
            return True
        else:
            await message.answer(text="нет такого цвета")


class IsSize(BaseFilter):
    async def __call__(self, message: Message = None) -> bool:
        if message.text in settings.PRICE_LIST["size"].keys():
            return True
        else:
            await message.answer(text="нет такого размера")


class IsCoverage(BaseFilter):
    async def __call__(self, message: Message = None) -> bool:
        if message.text in settings.PRICE_LIST["coverage"].keys():
            return True
        else:
            await message.answer(text="нет такого варианта ответа")
