from core.constants import EXIT
from telebot import types


class UnathorizedMenuScreen:

    WELCOME_TEXT = "Вітання! Я буду тобі допомагати протягом усього спілкування в групі інвесторів ЖК Паркова Долина"
    RULES_NOTICE = "Прошу ознайомитися з правилами."

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(
            row_width=2, resize_keyboard=1)
        keyboard.add(
            types.KeyboardButton(text="📋Правила")
        )
        self.bot.send_message(
            message.chat.id, f"{self.WELCOME_TEXT}\n\n{self.RULES_NOTICE}", reply_markup=keyboard)

    @staticmethod
    def match(message):
        if message.text.startswith(EXIT) or message.text.startswith("Головне меню"):
            return True
        return False
