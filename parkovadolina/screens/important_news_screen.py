from telebot import types
from datetime import datetime

class ImportantNewsScreen:

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    def screen(self, message):
        news_list = self.dao.important_news.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        
        if not news_list:
            self.bot.send_message(message.chat.id, "Вибачте поки немає важливих новин.", reply_markup=keyboard, parse_mode='HTML')
        else:
            self.bot.send_message(message.chat.id, "<b>Новини за тиждень:</b>\n\n", parse_mode='HTML')
            for news in news_list:
                date = datetime.fromtimestamp(int(news.date)).strftime('%Y-%m-%d %H:%M:%S')
                message_text = (
                    f"{news.text}\n"
                    f"{date} - @{news.username}"
                )
                self.bot.send_message(message.chat.id, message_text)
            self.bot.send_message(message.chat.id, f"---------------", reply_markup=keyboard, parse_mode='HTML')

    @staticmethod
    def match(message):
        return message.text.startswith("Важливі новини") or False