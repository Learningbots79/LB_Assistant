from typing import cast

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, Update, User
from telegram.ext import ContextTypes
from telegram.helpers import mention_html

from Assistant.database.block_db import is_banned_user
from Assistant.database.users_db import add_served_user
from config import LOGGER_ID, OWNER_ID


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = cast(User, update.effective_user)
    message = cast(Message, update.effective_message)
    owner = await context.bot.get_chat(OWNER_ID)
    if await is_banned_user(message.from_user.id):
        return

    #return

    button = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="join",
                    url=f"https://t.me/New_Color_Games",
                ),
                InlineKeyboardButton(
                    text="join",
                    url=f"https://t.me/AnnaClubIndia",
                ),
                InlineKeyboardButton(
                    text="join",
                    url=f"https://t.me/+EMTYcJGIPkZiYjk1",
                ),
            ],
        ]
    )
    new_user = await add_served_user(message.from_user.id)
    if new_user:
        await context.bot.send_message(
            chat_id=LOGGER_ID,
            text=f"<b>ɴᴇᴡ ᴜsᴇʀ :</b>\nᴜsᴇʀ: {mention_html(user.id, user.first_name)}\n<b>ᴜsᴇʀɴᴀᴍᴇ:</b> {user.username}\n<b>ɪᴅ:</b> <code>{user.id}</code>",
        )
    await message.reply_photo(
        "https://graph.org/file/ba8cf75fb71f22aa76b74.jpg",
        caption=f"..\n\nʜᴇʟʟᴏ 👋{mention_html(user.id, user.first_name)}.\n\n📝 ᴀssɪsᴛᴀɴᴛ ᴏғ {mention_html(owner.id, owner.first_name)}\nғᴇᴇʟ ғʀᴇᴇ ᴛᴏ sᴇɴᴅ ᴍᴇssᴀɢᴇ ʜᴇʀᴇ, ᴅᴏɴ'ᴛ ᴅᴍ",
        reply_markup=button,
    )
    return
