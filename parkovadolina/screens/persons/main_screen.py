from aiogram import types
from aiogram.types.message import ParseMode
from core.constants import EXIT

class PersonsScreen:

    SECTIONS = [EXIT]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        persons = self.dao.persons.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        for i in persons:
            keyboard.add(types.KeyboardButton(text=f"Персона, {i.full_name}"))
        keyboard.add(types.KeyboardButton(text=EXIT))
        await self.bot.send_message(message.chat.id, "Оберить персону.", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return True if message.text.startswith("🧩Персони") else False
            