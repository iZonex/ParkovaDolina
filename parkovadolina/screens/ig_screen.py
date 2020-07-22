from telebot import types
from core.constants import EXIT

class IGScreen:

    SECTIONS = [EXIT]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        text_body = self.dao.ig.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text=EXIT))
        self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode='HTML')

    @staticmethod
    def match(message):
        return message.text.startswith("🎖Iніціативна група") or False