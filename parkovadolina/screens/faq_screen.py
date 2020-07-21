from telebot import types

class FAQScreen:

    SECTIONS = ["🚪Вихід"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def details(self, message):
        question = message.text.split("Запитання, ")[1]
        faq = self.dao.faq.get_answer_by_question(question)
        message_text = f"{faq.answer}\n\n"
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text="Відповіді на запитання"))
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, message_text, reply_markup=keyboard)

    def menu(self, message):
        faqs = self.dao.faq.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        for i in faqs:
            keyboard.add(types.KeyboardButton(text=f"Запитання, {i.question}"))
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, "Оберить зпитання.", reply_markup=keyboard)

    def screen(self, message):
        if message.text.startswith("Запитання,"):
            self.details(message)
        else:
            self.menu(message)

    @staticmethod
    def match(message):
        if message.text.startswith("Запитання,") or message.text.startswith("🔍Відповіді на запитання"):
            return True
        return False
