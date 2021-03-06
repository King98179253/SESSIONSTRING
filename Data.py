from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
๐๐ฒ๐ ๐คจ {}

Welcome to {}

๐ฌ๐ผ๐ ๐๐ฎ๐ป ๐จ๐๐ฒ ๐ ๐ฒ ๐ง๐ผ ๐๐ฒ๐ป๐ฒ๐ฟ๐ฎ๐๐ฒ ๐ฃ๐๐ฟ๐ผ๐ด๐ฟ๐ฎ๐บ ๐๐ป๐ฑ ๐ง๐ฒ๐น๐ฒ๐๐ต๐ผ๐ป ๐ฆ๐๐ฟ๐ถ๐ป๐ด ๐ฆ๐ฒ๐๐๐ถ๐ผ๐ป. ๐จ๐๐ฒ ๐๐ฒ๐น๐ผ๐ ๐๐๐๐๐ผ๐ป๐ ๐ง๐ผ ๐๐ฒ๐ฎ๐ฟ๐ป ๐ ๐ผ๐ฟ๐ฒ !

By @SUBHI_WORLD
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("โ๏ธ๐ฆ๐ง๐๐ฅ๐ง ๐๐ฅ๐๐๐ง๐ ๐ฆ๐๐ฆ๐ฆ๐๐ข๐กโ๏ธ", callback_data="generate")],
        [InlineKeyboardButton(text="๐  Return Home ๐ ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("โ๏ธ ๐ฆ๐ง๐๐ฅ๐ง ๐๐๐ก๐๐ฅ๐๐ง๐๐ก๐ ๐ฆ๐๐ฆ๐ฆ๐๐ข๐กโ๏ธ", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("โ๏ธ๐ฆ๐ง๐๐ฅ๐ง ๐๐ฅ๐๐๐ง๐ ๐ฆ๐๐ฆ๐ฆ๐๐ข๐กโ๏ธ", callback_data="generate")],
        [InlineKeyboardButton("๐ค ๐๐ผ๐ ๐ง๐ผ ๐จ๐๐ฒ ๐ ๐ฒ ๐ค", callback_data="help")],
        [InlineKeyboardButton("โ๐ฆ๐จ๐ฃ๐ฃ๐ข๐ฅ๐ง ๐๐ฅ๐ข๐จ๐ฃโ", url="https://t.me/SUBHI_WORLD")],
        [InlineKeyboardButton("โ๏ธ๐ ๐ฌ ๐ข๐ช๐ก๐๐ฅ๐", url="https://t.me/ZINDA_H_TU_MERE_LIYE_HEART_HACK")],
        [InlineKeyboardButton("โจ๐๐๐ข๐จ๐ง๐", url="https://t.me/A_BUT")],
    ]

    # Help Message
    HELP = """
โจ **Available Commands** โจ

/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""
