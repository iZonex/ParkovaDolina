from telebot import types

class ChatsListScreen:

    SECTIONS = ["🚪Вихід"]

    CHATS = {
        "Чат Будинка №1 секція №1": "http://t.me/parkovadolyna1",
        "Чат Будинка №1 секція №2": "http://t.me/parkovadolyna2",
        "Чат Будинка №1 секція №3": "http://t.me/parkovadolyna3",
        "Чат Будинка №1 секція №4": "http://t.me/parkovadolyna4",
        "Чат Будинка №1 секція №5": "http://t.me/parkovadolyna5",
        "Чат Будинка №1 секція №6": "http://t.me/parkovadolyna6",
        "Чат Будинка №1 секція №7": "http://t.me/parkovadolyna7",
        "Чат Будинка №1 секція №8": "http://t.me/parkovadolyna8",
        "Чат Будинка №1 секція №9": "http://t.me/parkovadolyna9",
        "Чат Будинка №2": "http://t.me/parkovadolyna_2",
    }

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        bulding_chat = self.CHATS.get(message.text, None)
        if bulding_chat:
            text_body = f"Посилання на чат {message.text}:\n{bulding_chat}"
            self.bot.send_message(message.chat.id, text_body)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
            for i in self.CHATS.keys():
                keyboard.add(types.KeyboardButton(text=i))
            keyboard.add(types.KeyboardButton(text="🚪Вихід"))
            self.bot.send_message(message.chat.id, "Оберіть вашу секцію.", reply_markup=keyboard)

    @staticmethod
    def match(message):
        if message.text.startswith("Чати інвесторів") or message.text.startswith("Чат"):
            return True
        return False