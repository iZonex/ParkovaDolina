from telebot import types
from core.constants import EXIT

class PersonsScreen:

    SECTIONS = [EXIT]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        persons = self.dao.persons.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        for i in persons:
            keyboard.add(types.KeyboardButton(text=f"Персона, {i.full_name}"))
        keyboard.add(types.KeyboardButton(text=EXIT))
        self.bot.send_message(message.chat.id, "Оберить персону.", reply_markup=keyboard)

    @staticmethod
    def match(message):
        return True if message.text.startswith("🧩Персони") else False
            