from telebot import types

class CommunicationScreen:

    SECTIONS = ["Чати інвесторів", "Форум інвесторів", "🚪Вихід"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(*self.sections)
        self.bot.send_message(message.chat.id, "Оберіть тип зв'язку.", reply_markup=keyboard)

    @staticmethod
    def match(message):
        return message.text.startswith("👂Комунікація") or False