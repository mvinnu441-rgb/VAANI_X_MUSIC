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
from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from config import *
from VAANIMUSIC import app
from VAANIMUSIC.core.call import VAANI 
from VAANIMUSIC.utils import bot_sys_stats
from VAANIMUSIC.utils.decorators.language import language
from VAANIMUSIC.utils.inline import supp_markup
from config import BANNED_USERS, SHASHANK_IMG
import random


@app.on_message(filters.command("ping", prefixes=["/"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()

    response = await message.reply_photo(
        random.choice(SHASHANK_IMG),
        caption=_["ping_1"].format(app.mention),
    )

    UP, CPU, RAM, DISK = await bot_sys_stats()

    resp = (datetime.now() - start).total_seconds() * 1000

    # PyTgCalls ping removed because it causes _binding error
    pytgping = round(resp, 2)

    await response.edit_caption(
        _["ping_2"].format(
            round(resp, 2),
            app.mention,
            UP,
            RAM,
            CPU,
            DISK,
            pytgping
        ),
        reply_markup=supp_markup(_),
    )
