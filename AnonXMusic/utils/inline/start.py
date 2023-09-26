from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✚  𝐀ᴅᴅ 𝐌ᴇ 𝐈ɴ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="🤔 𝐇ᴇʟᴘ 🤔", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=""🌟 𝐆ʀᴏᴜᴘ 🌟", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="💌 𝐂ʜᴀɴɴᴇʟ 💌", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="🥀 𝐎ᴡɴᴇʀ 🥀", user_id=config.OWNER_ID),
            InlineKeyboardButton(
            text="❄️ 𝐔ᴘᴅᴀᴛᴇꜱ ❄️", url=f"https://t.me/FileStore_Bots_Updates"),
        ],
    ]
    return buttons
