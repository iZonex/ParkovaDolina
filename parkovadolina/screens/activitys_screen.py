from telebot import types

class ActivitysScreen:

    SECTIONS = ["🚪Вихід"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def screen(self, message):
        activitys = self.dao.activity.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        if not activitys:
            text_body = "Немає активності"
            self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard,)
        for i in activitys:
            text_body = (
                f'<strong>{i.title.upper()}</strong>\n'
                f"{i.due_date} - <b>{i.status}</b>\n\n"
                f"{i.actions_description} \n\n"
                f'<a href="{i.source_link}">Посилання</a>'
            )
            self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode='HTML')

    @staticmethod
    def match(message):
        return message.text.startswith("Активності") or False