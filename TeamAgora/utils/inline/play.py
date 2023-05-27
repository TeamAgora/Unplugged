import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUPPORT_CHANNEL, SUPPORT_GROUP
from TeamAgora import app

import config
from TeamAgora.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "💥TEAM-AGORA💥"
    elif 2 < anon < 3:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 3 <= anon < 4:
        bar = "💥TEAM-AGORA💥"
    elif 4 <= anon < 5:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 6 <= anon < 7:
        bar = "💥TEAM-AGORA💥"
    elif 7 <= anon < 8:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 9 <= anon < 10:
        bar = "💥𝙰TEAM-AGORA💥"
    elif 11 <= anon < 12:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 12 <= anon < 13:
        bar = "💥TEAM-AGORA💥"
    elif 13 < anon < 14:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 14 <= anon < 15:
        bar = "💥TEAM-AGORA💥"
    elif 15 <= anon < 16:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 16 <= anon < 17:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 17 <= anon < 18:
        bar = "💥TEAM-AGORA💥"
    elif 18 <= anon < 19:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 19 <= anon < 20:
        bar = "💥TEAM-AGORA💥"
    elif 20 <= anon < 21:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 21 <= anon < 22:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 22 <= anon < 23:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 23 <= anon < 24:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 24 <= anon < 25:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 25 <= anon < 26:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 26 <= anon < 27:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 27 <= anon < 28:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 28 <= anon < 29:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 29 <= anon < 30:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 30 <= anon < 31:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 31 <= anon < 32:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 32 <= anon < 33:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 33 <= anon < 34:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 34 <= anon < 35:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 35 <= anon < 36:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 36 <= anon < 37:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 37 <= anon < 38:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 38 <= anon < 39:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 39 <= anon < 40:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 40 <= anon < 41:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 41 <= anon < 42:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 42 <= anon < 43:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 43 <= anon < 44:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 44 < anon < 45:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 45 <= anon < 46:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 46 <= anon < 47:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 47 <= anon < 48:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 48 <= anon < 49:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 49 <= anon < 50:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 50 <= anon < 51:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 51 <= anon < 52:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 52 <= anon < 53:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 53 <= anon < 54:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 54 <= anon < 55:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 55 <= anon < 56:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 56 <= anon < 57:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 57 <= anon < 58:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 58 <= anon < 59:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 59 <= anon < 60:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 60 <= anon < 61:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 61 <= anon < 62:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 62 <= anon < 63:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 63 <= anon < 64:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 64 <= anon < 65:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 65 <= anon < 66:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 66 <= anon < 67:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 67 <= anon < 68:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 68 <= anon < 69:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 69 <= anon < 70:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 70 <= anon < 71:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 71 <= anon < 72:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 72 <= anon < 73:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 73 <= anon < 74:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 74 <= anon < 75:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 75 <= anon < 76:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 76 < anon < 77:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 77 <= anon < 78:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 78 <= anon < 79:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 79 <= anon < 80:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 80 <= anon < 81:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 81 <= anon < 82:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 82 <= anon < 83:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 83 <= anon < 84:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 84 <= anon < 85:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 85 <= anon < 86:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 86 <= anon < 87:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 87 <= anon < 88:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 88 <= anon < 89:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 89 <= anon < 90:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 90 <= anon < 91:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 91 <= anon < 92:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 92 <= anon < 93:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 93 <= anon < 94:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 94 <= anon < 95:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 95 <= anon < 96:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 96 <= anon < 97:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 97 <= anon < 98:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"
    elif 98 <= anon < 99:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    else:
        bar = "💥𝙰𝙻𝙾𝙽𝙴_𝙲𝚁𝙴𝙰𝚃𝙾𝚁𝚂💥"

        buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{dur} {bar} {played}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 2:
        bar = "💥TEAM-AGORA💥"
    elif 2 < anon < 3:
        bar = "🥀MR-AGORA🥀"
    elif 3 <= anon < 4:
        bar = "💥TEAM-AGORA💥"
    elif 4 <= anon < 5:
        bar = "🥀MR-AGORA🥀"
    elif 6 <= anon < 7:
        bar = "💥TEAM-AGORA💥"
    elif 7 <= anon < 8:
        bar = "🥀MR-AGORA🥀"
    elif 9 <= anon < 10:
        bar = "💥TEAM-AGORA💥"
    elif 11 <= anon < 12:
        bar = "🥀MR-AGORA🥀"
    elif 12 <= anon < 13:
        bar = "💥TEAM-AGORA💥"
    elif 13 < anon < 14:
        bar = "🥀MR-AGORA🥀"
    elif 14 <= anon < 15:
        bar = "💥TEAM-AGORA💥"
    elif 15 <= anon < 16:
        bar = "🥀MR-AGORA🥀"
    elif 16 <= anon < 17:
        bar = "🥀MR-AGORA🥀"
    elif 17 <= anon < 18:
        bar = "💥TEAM-AGORA💥"
    elif 18 <= anon < 19:
        bar = "🥀MR-AGORA🥀"
    elif 19 <= anon < 20:
        bar = "💥TEAM-AGORA💥"
    elif 20 <= anon < 21:
        bar = "🥀MR-AGORA🥀"
    elif 21 <= anon < 22:
        bar = "💥TEAM-AGORA💥"
    elif 22 <= anon < 23:
        bar = "🥀MR-AGORA🥀"
    elif 23 <= anon < 24:
        bar = "💥TEAM-AGORA💥"
    elif 24 <= anon < 25:
        bar = "🥀MR-AGORA🥀"
    elif 25 <= anon < 26:
        bar = "💥TEAM-AGORA💥"
    elif 26 <= anon < 27:
        bar = "🥀MR-AGORA🥀"
    elif 27 <= anon < 28:
        bar = "💥TEAM-AGORA💥"
    elif 28 <= anon < 29:
        bar = "🥀MR-AGORA🥀"
    elif 29 <= anon < 30:
        bar = "💥TEAM-AGORA💥"
    elif 30 <= anon < 31:
        bar = "🥀MR-AGORA🥀"
    elif 31 <= anon < 32:
        bar = "💥TEAM-AGORA💥"
    elif 32 <= anon < 33:
        bar = "🥀MR-AGORA🥀"
    elif 33 <= anon < 34:
        bar = "💥TEAM-AGORA💥"
    elif 34 <= anon < 35:
        bar = "🥀MR-AGORA🥀"
    elif 35 <= anon < 36:
        bar = "💥TEAM-AGORA💥"
    elif 36 <= anon < 37:
        bar = "🥀MR-AGORA🥀"
    elif 37 <= anon < 38:
        bar = "💥TEAM-AGORA💥"
    elif 38 <= anon < 39:
        bar = "🥀MR-AGORA🥀"
    elif 39 <= anon < 40:
        bar = "💥TEAM-AGORA💥"
    elif 40 <= anon < 41:
        bar = "🥀MR-AGORA🥀"
    elif 41 <= anon < 42:
        bar = "💥TEAM-AGORA💥"
    elif 42 <= anon < 43:
        bar = "🥀MR-AGORA🥀"
    elif 43 <= anon < 44:
        bar = "💥TEAM-AGORA💥"
    elif 44 < anon < 45:
        bar = "🥀MR-AGORA🥀"
    elif 45 <= anon < 46:
        bar = "💥TEAM-AGORA💥"
    elif 46 <= anon < 47:
        bar = "🥀MR-AGORA🥀"
    elif 47 <= anon < 48:
        bar = "💥TEAM-AGORA💥"
    elif 48 <= anon < 49:
        bar = "🥀MR-AGORA🥀"
    elif 49 <= anon < 50:
        bar = "💥TEAM-AGORA💥"
    elif 50 <= anon < 51:
        bar = "🥀MR-AGORA🥀"
    elif 51 <= anon < 52:
        bar = "💥TEAM-AGORA💥"
    elif 52 <= anon < 53:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 53 <= anon < 54:
        bar = "💥TEAM-AGORA💥"
    elif 54 <= anon < 55:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 55 <= anon < 56:
        bar = "💥TEAM-AGORA💥"
    elif 56 <= anon < 57:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 57 <= anon < 58:
        bar = "💥TEAM-AGORA💥"
    elif 58 <= anon < 59:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 59 <= anon < 60:
        bar = "💥TEAM-AGORA💥"
    elif 60 <= anon < 61:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 61 <= anon < 62:
        bar = "💥TEAM-AGORA💥"
    elif 62 <= anon < 63:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 63 <= anon < 64:
        bar = "💥TEAM-AGORA💥"
    elif 64 <= anon < 65:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 65 <= anon < 66:
        bar = "💥TEAM-AGORA💥"
    elif 66 <= anon < 67:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 67 <= anon < 68:
        bar = "💥TEAM-AGORA💥"
    elif 68 <= anon < 69:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 69 <= anon < 70:
        bar = "💥TEAM-AGORA💥"
    elif 70 <= anon < 71:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 71 <= anon < 72:
        bar = "💥TEAM-AGORA💥"
    elif 72 <= anon < 73:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 73 <= anon < 74:
        bar = "💥TEAM-AGORA💥"
    elif 74 <= anon < 75:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 75 <= anon < 76:
        bar = "💥TEAM-AGORA💥"
    elif 76 < anon < 77:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 77 <= anon < 78:
        bar = "💥TEAM-AGORA💥"
    elif 78 <= anon < 79:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 79 <= anon < 80:
        bar = "💥TEAM-AGORA💥"
    elif 80 <= anon < 81:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 81 <= anon < 82:
        bar = "💥TEAM-AGORA💥"
    elif 82 <= anon < 83:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 83 <= anon < 84:
        bar = "💥TEAM-AGORA💥"
    elif 84 <= anon < 85:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 85 <= anon < 86:
        bar = "💥TEAM-AGORA💥"
    elif 86 <= anon < 87:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 87 <= anon < 88:
        bar = "💥TEAM-AGORA💥"
    elif 88 <= anon < 89:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 89 <= anon < 90:
        bar = "💥TEAM-AGORA💥"
    elif 90 <= anon < 91:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 91 <= anon < 92:
        bar = "💥TEAM-AGORA💥"
    elif 92 <= anon < 93:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 93 <= anon < 94:
        bar = "💥TEAM-AGORA💥"
    elif 94 <= anon < 95:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 95 <= anon < 96:
        bar = "💥TEAM-AGORA💥"
    elif 96 <= anon < 97:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    elif 97 <= anon < 98:
        bar = "💥TEAM-AGORA💥"
    elif 98 <= anon < 99:
        bar = "🥀𝙸𝚃𝚉_𝙰𝙻𝙾𝙽𝙴🥀"
    else:
        bar = "💥TEAM-AGORA💥"
        
        buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{dur} {bar} {played}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
           InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons  = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ]
    ]
    return buttons


## Search Query Inline


def track_markup(_,chat_id, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
        [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, chat_id, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"anonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"anonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ ᴄʟᴏsᴇ ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/KIMJIKOINBOT?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="❚❚", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="☆", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="💥🔥DEVELOPER🔥💥", url="https://t.me/AGORAWORLD"
            ),
        ],
         [
            InlineKeyboardButton(
                text="《 10",
                callback_data=f"ADMIN 1|{chat_id}",
            ),
            

            InlineKeyboardButton(
                text="✯ ᴄʟᴏsᴇ ✯", callback_data=f"close",
            ),

            InlineKeyboardButton(
                text="10 》",
                callback_data=f"ADMIN 2|{chat_id}",
            ),
        ],
    ]
    return buttons
