from telebot import types

class PersonsScreen:

    SECTIONS = ["🚪Вихід"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def menu(self, message):
        persons = self.dao.persons.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        for i in persons:
            keyboard.add(types.KeyboardButton(text=f"Персона, {i.full_name}"))
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, "Оберить персону.", reply_markup=keyboard)

    def details(self, message):
        person_full_name = message.text.split("Персона, ")[1]
        person = self.dao.persons.get_person_by_full_name(full_name=person_full_name)
        message_text = (
            f"<strong>{person.full_name.upper()}</strong>\n\n"
            f'<a href="{person.photo}">&#8205;</a>'
            f"{person.short_description}\n"
            f'<a href="{person.link}">Посилання</a>\n\n'
        )
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text="Персони"))
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, message_text, reply_markup=keyboard, parse_mode="HTML")

    def screen(self, message):
        if message.text.startswith("Персона, "):
            self.details(message)
        else:
            self.menu(message)