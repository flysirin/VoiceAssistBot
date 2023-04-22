from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexicon.lexicon import LEXICON


def create_inline_kb(*args, **kwargs) -> InlineKeyboardMarkup:
    read_text_button: InlineKeyboardButton = InlineKeyboardButton(
        text="Press for read text",
        callback_data='read_text_button_pressed')
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[[read_text_button]])
    return keyboard

