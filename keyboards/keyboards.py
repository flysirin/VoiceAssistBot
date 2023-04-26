from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from lexicon.lexicon import LEXICON


def create_inline_kb(*args, **kwargs) -> InlineKeyboardMarkup:
    read_text_button: InlineKeyboardButton = InlineKeyboardButton(
        text="Press for read text",
        callback_data="read_text_button_pressed")
    send_text_open_ai_button: InlineKeyboardButton = InlineKeyboardButton(
        text="Send text to AI GPT 3.5",
        callback_data="send_text_open_ai"
    )
    keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
        inline_keyboard=[[read_text_button],
                         [send_text_open_ai_button]])
    return keyboard
