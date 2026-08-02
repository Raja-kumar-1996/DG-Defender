from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_USERNAME


def start_buttons():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "➕ Add Me",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                )
            ],
            [
                InlineKeyboardButton(
                    "📚 Commands",
                    callback_data="commands"
                ),
                InlineKeyboardButton(
                    "ℹ️ About",
                    callback_data="about"
                )
            ]
        ]
    )
