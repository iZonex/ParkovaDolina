from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import EXIT

class PersonsDetailScreen(Screen):

    SECTIONS = [EXIT]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        person_full_name = message.text.split("Персона, ")[1]
        person = self.dao.persons.get_person_by_full_name(full_name=person_full_name)
        message_text = (
            f"<strong>{person.full_name.upper()}</strong>\n\n"
            f'<a href="{person.photo}">&#8205;</a>'
            f"{person.short_description}\n"
            f'<a href="{person.link}">Посилання</a>\n\n'
        )
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text="↩️Назад"))
        keyboard.add(types.KeyboardButton(text=EXIT))
        await self.bot.send_message(message.chat.id, message_text, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return True if message.text.startswith("Персона,") else False
            