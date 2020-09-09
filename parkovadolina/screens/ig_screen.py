from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class IGScreen(Screen):

    SECTIONS = [MAIN_MENU]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        text_body = self.dao.ig.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text=MAIN_MENU))
        await self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("🎖Iніціативна група") or False