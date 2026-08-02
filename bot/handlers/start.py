from pyrogram import filters
from bot import app
from bot.keyboards.inline import start_buttons
from config import BOT_NAME


@app.on_message(filters.private & filters.command("start"))
async def start(_, message):

    text = f"""
**🛡 Welcome to {BOT_NAME}!**

Hello {message.from_user.mention} 👋

I'm a powerful Telegram Group Management Bot.

✨ Features

• Welcome System
• Rules Verification
• Captcha Verification
• Anti Spam
• Anti Raid
• Admin Tools
• Logs
• Notes
• Filters
• Games (Coming Soon)

Click the buttons below to get started.
"""

    await message.reply_text(
        text,
        reply_markup=start_buttons(),
        disable_web_page_preview=True
    )
