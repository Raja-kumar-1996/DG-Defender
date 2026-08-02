from pyrogram import filters
from pyrogram.types import CallbackQuery

from bot import app


@app.on_callback_query(filters.regex("^about$"))
async def about(_, query: CallbackQuery):

    await query.answer()

    await query.message.edit_text(
        """
🛡 **DG Defender**

Version: 1.0.0

A professional Telegram Group Management Bot.

Developer:
👨‍💻 DG Team
"""
    )


@app.on_callback_query(filters.regex("^commands$"))
async def commands(_, query: CallbackQuery):

    await query.answer()

    await query.message.edit_text(
        """
📚 **Available Commands**

/start
/help

More commands will be added soon.
"""
    )
