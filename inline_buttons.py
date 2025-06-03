from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

elon_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅",callback_data="1"),
            InlineKeyboardButton(text="❌",callback_data="0")
         ]
    ]
)