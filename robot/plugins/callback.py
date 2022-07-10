#
# Copyright (C) by Kutty-Angel@Github, < https://github.com/Kutty-Angel >.
#
# This file is part of < https://github.com/Kutty-Angel/robot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Kutty-Angel/robot/blob/main/LICENSE >
#
# All rights reserved !!


from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from robot.config import BOT_NAME, OWNER_USERNAME, UPDATE, SUPPORT, BOT_USERNAME


@Client.on_callback_query(filters.regex("home"))
async def home(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴡᴇʟᴄᴏᴍᴇ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴋᴜᴛᴛʏ ᴀɴɢᴇʟ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs.

ᴜsᴇ ɪɴʟɪɴᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ !!""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cmds"),
                    InlineKeyboardButton(
                        "🫂 sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ✚", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "🌏 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/{UPDATE}"),
                    InlineKeyboardButton(
                        "🔰 ᴏᴛʜᴇʀs", callback_data="others")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("others"))
async def others(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ʜᴇʏʏ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id})

ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀʙᴏᴜᴛ ᴍᴇ :""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗯️ ʜᴇʀᴏᴋᴜ", url=f"https://t.me/DuskyBotZUpdates"),
                    InlineKeyboardButton(
                        "🌐 ɢɪᴛʜᴜʙ", url=f"https://t.me/DuskyBotZUpdates")
                ],
                [
                    InlineKeyboardButton(
                        "🍭 ᴄʀᴇᴅɪᴛs", url=f"https://t.me/DuskyBotZUpdates"),
                    InlineKeyboardButton(
                        "🍀 ʀᴇᴘᴏ ɪɴғᴏ", url=f"https://t.me/DuskyBotZUpdates")
                ],
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="home")
                ]
           ]
        ),
    )


@Client.on_callback_query(filters.regex("credit"))
async def credit(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴄʀᴇᴅɪᴛs ғᴏʀ ᴛʜɪs ʙᴏᴛ 🍀

• @DuskyBotZSupport
- ʀᴇᴘᴏ ᴅᴇᴠᴇʟᴏᴘᴇʀ !! 

• @DuskyBotZUpdates
- sᴜᴘᴘᴏʀᴛ & ᴜᴘᴅᴀᴛᴇs ᴍᴀɪɴᴛᴀɪɴᴇʀ

• @{OWNER_USERNAME}
- ʙᴏᴛ ᴏᴡɴᴇʀ


ᴛʜᴀɴᴋs ᴀ ʟᴏᴛ ғᴏʀ ᴄᴏɴᴛʀɪʙᴜᴛɪɴɢ ʏᴏᴜʀ ᴛɪᴍᴇ ᴀɴᴅ sᴋɪʟʟs !!""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
    )



@Client.on_callback_query(filters.regex("repoinfo"))
async def repoinfo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ᴀʙᴏᴜᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : 

ᴛʜɪs ʀᴇᴘᴏ ɪs ᴏɴʟʏ ᴍᴀᴅᴇ ғᴏʀ ᴅᴇᴘʟᴏʏɪɴɢ ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ʙᴏᴛ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ғᴀᴄɪɴɢ ʜᴇʀᴏᴋᴜ ᴀᴄᴄᴏᴜɴᴛ ʙᴀɴɴɪɴɢ ᴘʀᴏʙᴇʟᴍ.

ғᴏɴᴛ ᴜsᴇᴅ : sᴍᴀʟʟ ᴄᴀᴘs

🔗 sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : https://t.me/KuttyAngelXUpdates""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⬅️ ʙᴀᴄᴋ", callback_data="others")
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
