from core.constants import EXIT
from telebot import types


class MainScreen:

    WELCOME_TEXT = "Вітання! Я буду тобі допомагати протягом усього спілкування в групі інвесторів ЖК Паркова Долина"
    RULES_NOTICE = "Прошу ознайомитися з правилами. Натисніть знизу кнопку 📋Правіла для продовження"
    SECTIONS = ["🗞Важливі новини", "🎖Iніціативна група", "🏗Будівництво",
                "🧩Персони", "👂Комунікація", "🗓Активності",
                "🔍Відповіді на запитання", "🤝Група підтверджених інвесторів"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        user = self.dao.users.get_by_user_id(message.from_user.id)
        if user:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
            keyboard.add(*self.sections)
            if message.text == "/start":
                self.bot.send_message(message.chat.id, self.WELCOME_TEXT, reply_markup=keyboard)
            else:
                self.bot.send_message(message.chat.id, "Головне меню", reply_markup=keyboard)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
            keyboard.add(types.KeyboardButton(text="📋Правила"))
            self.bot.send_message(message.chat.id, f"{self.WELCOME_TEXT}\n\n{self.RULES_NOTICE}", reply_markup=keyboard)

    @staticmethod
    def match(message):
        if message.text.startswith(EXIT) or message.text.startswith("Головне меню") or message.text.startswith("/start"):
            return True
        return False
