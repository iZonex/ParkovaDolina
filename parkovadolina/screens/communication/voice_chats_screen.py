from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class VoiceChatsScreen(Screen):

    SECTIONS = [MAIN_MENU]
    LINK = "https://discord.gg/XrTMwWz"

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def screen(self, message):
        text_body = f"Посилання на голосовий чат:\n{self.LINK}"
        await self.bot.send_message(message.chat.id, text_body, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("Голосовий чат") or False