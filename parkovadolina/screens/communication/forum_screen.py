from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class ForumScreen(Screen):

    SECTIONS = [MAIN_MENU]
    FORUM_LINK = "https://parkova-dolyna.com/"

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(*self.sections)
        text_body = f"Посилання на форум:\n{self.FORUM_LINK}"
        await self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("Форум інвесторів") or False