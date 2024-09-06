
from pyrogram import version
from bot import Bot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import *  # Import your UPI_ID and SCREENSHOT_URL here

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"» ᴄʀᴇᴀᴛᴏʀ: subaru\n"
                   f"» ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : ᴏᴛᴀᴋᴜғʟɪx ɴᴇᴛᴡᴏʀᴋ\n"
                   f"» ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ : ᴀɴɪᴍᴇ ᴄʀᴜɪsᴇ\n"
                   f"» sᴇʀɪᴇs ᴄʜᴀɴɴᴇʟ : ᴡᴇʙsᴇʀɪᴇs ғʟɪx\n"
                   f"» ᴀᴅᴜʟᴛ ᴍᴀɴʜᴡᴀ : ᴘᴏʀɴʜᴡᴀs\n"
                   f"» ᴅᴇᴠᴇʟᴏᴘᴇʀ : subaru",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data = "close")
                    ]
                ]
            )
        )
    # ... (rest of your callback handler code) ...
        # ... (Your 'close' section is fine) ...
    elif data == "buy_prem":
        await query.edit_message_text(
            text=f"👋 {query.from_user.username}\n\n"
                 f"🎖️ Available Plans :\n\n"
                 f"● {PRICE1} rs For 7 Days Prime Membership\n\n"
                 f"● {PRICE2} rs For 1 Month Prime Membership\n\n"
                 f"● {PRICE3} rs For 3 Months Prime Membership\n\n"
                 f"● {PRICE4} rs For 6 Months Prime Membership\n\n"
                 f"● {PRICE5} rs For 1 Year Prime Membership\n\n\n"
                 f"💵 UPI ID -  {UPI_ID}\n\n"
                 f"(Tap to copy UPI Id)\n\n\n"
                 f"📸 QR - ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ ({UPI_IMAGE_URL})\n\n"
                 f"• ғɪʀsᴛ sᴛᴇᴘ : ᴘᴀʏ ᴛʜᴇ ᴀᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ғᴀᴠᴏʀɪᴛᴇ ᴘʟᴀɴ ᴛᴏ ᴛʜɪs {UPI_ID} ᴜᴘɪ ɪᴅ.\n"
                 f"• secoɴᴅ sᴛᴇᴘ : ᴛᴀᴋᴇ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴀɴᴅ sʜᴀʀᴇ ɪᴛ ᴅɪʀᴇᴄᴛʟʏ ʜᴇʀᴇ: @Sourav00876.\n"
                 f"• ᴀʟᴛᴇʀɴᴀᴛɪᴠᴇ sᴛᴇᴘ : ᴏʀ ᴜᴘʟᴏᴀᴅ ᴛʜᴇ sᴄʀᴇᴇɴsʜᴏᴛ ʜᴇʀᴇ ᴀɴᴅ ʀᴇᴘʟʏ ᴡɪᴛʜ the /bought ᴄᴏᴍᴍᴀɴᴅ.\n\n"
                 f"Yᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴ ᴡɪʟʟ ʙᴇ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴀғᴛᴇʀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ",
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [   
                    [
                        InlineKeyboardButton("• sᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ sᴄʀᴇᴀsʜᴏᴛ •", url=(SCREENSHOT_URL))
                    ],
                    [
                        InlineKeyboardButton("• ᴄʟᴏsᴇ •", callback_data = "close")
                    ]
                ]
            )
        )
