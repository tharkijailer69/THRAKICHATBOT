
import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from ROYEDITX import BOT_NAME, LOCOPILOT, dev
from ROYEDITX.database.chats import add_served_chat
from ROYEDITX.database.users import add_served_user
from ROYEDITX.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_START,
)


@dev.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        accha = await m.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("👻")
        await asyncio.sleep(0.2)
        await accha.edit("🌼")
        await asyncio.sleep(0.2)
        await accha.edit("🏵️")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""❖ ʜᴇʏ ᴄʜᴜᴛɪʏᴀ ʀᴀɴᴅɪʙᴀᴀᴢ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ♥︎\n\n⬤ ɪ ᴀᴍ {BOT_NAME}, ᴀɪ ʙᴀsᴇ ᴛʜᴀʀᴋɪ ᴄʜᴀᴛʙᴏᴛ.\n⬤ ᴍᴀɪɴ ᴛᴇʀᴀ ᴅᴇᴀᴅ ɢʀᴏᴜᴘ ᴋᴏ ᴀᴄᴛɪᴠᴇ  ɢʀᴏᴜᴘ ʙɴᴀ sᴋᴛɪ ʜᴜ.\n\n❖ ᴛᴀᴘ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ᴛᴏ sᴇᴇ ᴀʟʟ ᴍʏ ᴛʜᴀʀᴋɪ ᴄᴏᴍᴍᴀɴᴅs.""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
 ##############

@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help(client: LOCOPILOT, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        hmm = await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""❖ ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ꜰᴏʀ {BOT_NAME}\n\n⬤ /ping ➥ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ ᴏʀ ɴᴏᴛ.\n⬤ /stats ➥ ᴄʜᴇᴄᴋ ᴍʏ ᴄʜᴀᴛs sᴛᴀᴛs.\n⬤ /chatbot ➥ ᴇɴᴀʙʟᴇ/ᴅɪsᴀʙʟᴇ [ᴡᴏʀᴋ ᴏɴʟʏ ɢʀᴏᴜᴘ]\n\n❖ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ ➠ /""",
            reply_markup=InlineKeyboardMarkup(HELP_BTN),
        )
  #############

@dev.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    await m.reply_text(
        text= f"""❖ ʜᴇʏ ᴄʜᴜᴛɪʏᴀ ʀᴀɴᴅɪʙᴀᴀᴢ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ ♥︎\n\n⬤ ɪ ᴀᴍ {BOT_NAME},  ᴀɪ ʙᴀsᴇ ᴛʜᴀʀᴋɪ ᴄʜᴀᴛʙᴏᴛ.\n\n❖ ɪғ ʏᴏᴜ ᴡᴀɴᴛ {BOT_NAME} ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.""",
        reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
        disable_web_page_preview=True,
    )
#########______--------+-------______####$$$$$
