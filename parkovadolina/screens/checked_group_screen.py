from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class CheckedGroupScreen(Screen):

    SECTIONS = [MAIN_MENU]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def screen(self, message):
        text_body = self.dao.checked_group.get()
        await self.bot.send_message(message.chat.id, text_body, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("🤝Група підтверджених інвесторів") or False