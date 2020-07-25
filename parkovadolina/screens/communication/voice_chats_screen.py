from telebot import types
from core.constants import EXIT

class VoiceChatsScreen:

    SECTIONS = [EXIT]
    LINK = "https://discord.gg/XrTMwWz"

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(*self.sections)
        text_body = f"Посилання на голосовий чат:\n{self.LINK}"
        self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard)

    @staticmethod
    def match(message):
        return message.text.startswith("Голосовий чат") or False