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

    async def menu(self, message):
        persons = self.dao.persons.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        for i in persons:
            keyboard.add(types.KeyboardButton(text=f"Персона, {i.full_name}"))
        keyboard.add(types.KeyboardButton(text=EXIT))
        await self.bot.send_message(message.chat.id, "Оберить персону.", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    async def details(self, message):
        person_full_name = message.text.split("Персона, ")[1]
        person = self.dao.persons.get_person_by_full_name(full_name=person_full_name)
        message_text = (
            f"<strong>{person.full_name.upper()}</strong>\n\n"
            f'<a href="{person.photo}">&#8205;</a>'
            f"{person.short_description}\n"
            f'<a href="{person.link}">Посилання</a>\n\n'
        )
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text="🧩Персони"))
        keyboard.add(types.KeyboardButton(text=EXIT))
        await self.bot.send_message(message.chat.id, message_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    async def screen(self, message):
        if message.text.startswith("Персона, "):
            await self.details(message)
        else:
            await self.menu(message)

    @staticmethod
    def match(message):
        if message.text.startswith("Персона,") or message.text.startswith("🧩Персони"):
            return True
        return False

            