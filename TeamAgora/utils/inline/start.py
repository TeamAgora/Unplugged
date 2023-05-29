from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋 TAKE ME WITH YOU 🦋",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="🦋 COMMANDS 🦋",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="🦋 SETTINGS 🦋", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🦋 UPDATES 🦋", url=f"https://t.me/TEAMAGORA"),
            InlineKeyboardButton(
                text="🦋 SUPPORT 🦋", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = "https://t.me/MR_AGORA"):
    buttons = [
        [
            InlineKeyboardButton(
                text="🦋 TAKE ME WITH YOU 🦋",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🦋 COMMANDS 🦋", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="🦋 UPDATE 🦋", url=f"https://t.me/TEAMAGORA"),
            InlineKeyboardButton(
                text="🦋 SUPORT 🦋", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="𓊈🦋 DEVELOPER 🦋𓊉", url=f"https://t.me/MR_AGORA"
                )
        ],
     ]
    return buttons
