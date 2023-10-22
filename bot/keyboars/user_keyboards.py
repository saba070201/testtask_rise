from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

color_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="красный")],
        [KeyboardButton(text="светлый")],
        [KeyboardButton(text="темный")],
    ],
    resize_keyboard=True,
)
coverage_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="да", callback_data="yes")],
        [InlineKeyboardButton(text="нет", callback_data="no")],
    ],
)
