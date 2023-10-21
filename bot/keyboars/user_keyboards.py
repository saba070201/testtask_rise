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
coverage_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="да")],
        [KeyboardButton(text="нет")],
    ],
    resize_keyboard=True,
)
