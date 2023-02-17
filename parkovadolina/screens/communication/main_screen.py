from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class CommunicationScreen(Screen):

    SECTIONS = ["Чати інвесторів", "Контакти", MAIN_MENU]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(*self.sections)
        await self.bot.send_message(message.chat.id, "Оберіть тип зв'язку.", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    def match_context(self, message):
        return message.text.startswith("↩️Назад")

    @staticmethod
    def match(message):
        return message.text.startswith("👂Комунікація") or False