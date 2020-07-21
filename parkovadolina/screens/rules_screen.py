from telebot import types

class RulesScreen:

    SECTIONS = ["🚪Вихід"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def rules_confirm(self, message):
        user_id = message.from_user.id
        self.dao.users.create(user_id)
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, "Дякую за те що прийняли правила", reply_markup=keyboard)

    def rules_chats(self, message):
        text_body = "📋 Правила чату:\n\n"
        text_body += "\n\n".join(self.dao.rules.get())
        available_options = ["🤝Згоден з правилами"]
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        [ keyboard.add(types.KeyboardButton(text=i)) for i in available_options]
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard)

    def screen(self, message):
        if message.text.startswith("🤝Згоден з правилами"):
            self.rules_confirm(message)
        else:
            self.rules_chats(message)

    @staticmethod
    def match(message):
        if message.text.startswith("🤝Згоден з правилами") or message.text.startswith("📋Правила"):
            return True
        return False