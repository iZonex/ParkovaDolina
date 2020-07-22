from telebot import types


class MainScreen:

    WELCOME_TEXT = "Вітання! Я буду тобі допомагати протягом усього спілкування в групі інвесторів ЖК Паркова Долина"
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
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(*self.sections)
        if message.text == "/start":
            self.bot.send_message(
                message.chat.id, self.WELCOME_TEXT, reply_markup=keyboard)
        else:
            self.bot.send_message(
                message.chat.id, "Головне меню", reply_markup=keyboard)
