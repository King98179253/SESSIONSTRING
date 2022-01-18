from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
𝗛𝗲𝘆 🤨 {}

Welcome to {}

𝗬𝗼𝘂 𝗖𝗮𝗻 𝗨𝘀𝗲 𝗠𝗲 𝗧𝗼 𝗚𝗲𝗻𝗲𝗿𝗮𝘁𝗲 𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 𝗔𝗻𝗱 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝗦𝘁𝗿𝗶𝗻𝗴 𝗦𝗲𝘀𝘀𝗶𝗼𝗻. 𝗨𝘀𝗲 𝗕𝗲𝗹𝗼𝘄 𝗕𝘂𝘁𝘁𝗼𝗻𝘀 𝗧𝗼 𝗟𝗲𝗮𝗿𝗻 𝗠𝗼𝗿𝗲 !

By @SUBHI_WORLD
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("⚜️𝗦𝗧𝗔𝗥𝗧 𝗖𝗥𝗘𝗔𝗧𝗘 𝗦𝗘𝗦𝗦𝗜𝗢𝗡⚜️", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("⚜️ 𝗦𝗧𝗔𝗥𝗧 𝗚𝗘𝗡𝗘𝗥𝗔𝗧𝗜𝗡𝗚 𝗦𝗘𝗦𝗦𝗜𝗢𝗡⚜️", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("⚜️𝗦𝗧𝗔𝗥𝗧 𝗖𝗥𝗘𝗔𝗧𝗘 𝗦𝗘𝗦𝗦𝗜𝗢𝗡⚜️", callback_data="generate")],
        [InlineKeyboardButton("🤔 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲 🤔", callback_data="help")],
        [InlineKeyboardButton("➕𝗦𝗨𝗣𝗣𝗢𝗥𝗧 𝗚𝗥𝗢𝗨𝗣➕", url="https://t.me/SUBHI_WORLD")],
        [InlineKeyboardButton("⚜️𝗠𝗬 𝗢𝗪𝗡𝗘𝗥👑", url="https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK")],
        [InlineKeyboardButton("✨𝗔𝗕𝗢𝗨𝗧🎉", url="https://t.me/A_BUT")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""
