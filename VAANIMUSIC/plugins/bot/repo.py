from pyrogram import filters
from pyrogram.enums import ButtonStyle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VAANIMUSIC import app
from config import BOT_USERNAME
from VAANIMUSIC.utils.errors import capture_err
import httpx

# ── emoji_2e47b_by_TgEmodziBot pack IDs ──
_E_STAR   = 6073519257637884127   # 🌟
_E_HEART  = 6071046056555058251   # ❤️
_E_SPARK  = 6073301180673430006   # ✨
_E_GLOW   = 6073456529640525999   # 🤩
_E_FLOWER = 6073145973440253945   # 🌸
_E_LOVE   = 6073518286975276048   # 💗
_E_RIBBON = 6070857967052263096   # 🎀
_E_ROSE   = 6073547170630341250   # 🌹
_E_RIGHT  = 6073261718513913664   # ➡️
_E_BOUQ   = 6073117703965511893   # 💐

def e(eid, fb):
    return f'<emoji id={eid}>{fb}</emoji>'

start_txt = (
    f"{e(_E_STAR,'🌟')} {e(_E_GLOW,'🤩')} <b> | ᴍᴀᴅᴀʀᴀ</b> {e(_E_GLOW,'🤩')} {e(_E_STAR,'🌟')}\n\n"
    f"{e(_E_SPARK,'✨')} ʙᴀᴅᴀ ᴀᴀʏᴀ ʙᴏᴛ ᴋᴀ ʀᴇᴘᴏ ᴅᴇᴋʜɴᴇ,\n"
    f"{e(_E_LOVE,'💗')} ᴘᴀʜʟᴇ ᴀᴘɴɪ ʟɪɢᴇ ᴋᴀ ʀᴇᴘᴏ sᴜᴅʜᴀʀ ᴊᴀᴀᴋᴇ !\n\n"
    f"<pre>||{e(_E_RIGHT,'➡️')} ᴜᴩᴛɪᴍᴇ       :  𝟷ʜ:𝟹𝟺ᴍ:𝟻𝟺s\n"
    f"{e(_E_RIGHT,'➡️')} sᴛᴏʀᴀɢᴇ      :  𝟸𝟽.𝟺%\n"
    f"{e(_E_RIGHT,'➡️')} ᴄᴩᴜ ʟᴏᴀᴅ    :  𝟷𝟷.𝟸%\n"
    f"{e(_E_RIGHT,'➡️')} ʀᴀᴍ ᴜsᴇ     :  𝟷𝟽.𝟻%||</pre>\n\n"
    f"{e(_E_ROSE,'🌹')} ᴘᴏᴡєʀєᴅ ʙʏ» <a href=\"https://t.me/Call_me_Mr_Vinnu\">VANɪsᴀ ⌯</a>\n"
    f"{e(_E_BOUQ,'💐')} {e(_E_FLOWER,'🌸')} {e(_E_RIBBON,'🎀')} {e(_E_HEART,'❤️')}"
)


@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
            InlineKeyboardButton(
                text="˹ηєᴛᴡᴏʀᴋ˼",
                url="https://t.me/music_X_suppor",
                style=ButtonStyle.PRIMARY,
            ),
            InlineKeyboardButton(
                text="˹ϻʏ ʜᴏϻє˼",
                url="https://t.me/jhichichic",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            InlineKeyboardButton(
                text="˹ ϻʏ ϻᴧsᴛєʀ ˼ 👑",
                url="https://t.me/Zaviaan_exe",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]

    await msg.reply_photo(
        photo="https://i.supaimg.com/14ac9144-a5d0-49c4-9fc7-8c73f527216c/7bc9f0b7-9e84-470f-858f-b2f9f1ee88ba.png",
        caption=start_txt,
        reply_markup=InlineKeyboardMarkup(buttons),
    )
