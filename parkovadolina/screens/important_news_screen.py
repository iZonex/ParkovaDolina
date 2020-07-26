from aiogram import types
from aiogram.types import ParseMode
from datetime import datetime
from core.constants import EXIT

class ImportantNewsScreen:

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def screen(self, message):
        news_list = self.dao.important_news.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text=EXIT))
        
        if not news_list:
            await self.bot.send_message(message.chat.id, "Вибачте поки немає важливих новин.", reply_markup=keyboard, parse_mode=ParseMode.HTML)
        else:
            await self.bot.send_message(message.chat.id, "<b>Новини за тиждень:</b>\n\n", parse_mode=ParseMode.HTML)
            for news in news_list[::-1]:
                date = datetime.fromtimestamp(int(news.date)).strftime('%Y-%m-%d %H:%M:%S')
                message_text = (
                    f"{news.text}\n"
                    f"{date} - @{news.username}"
                )
                await self.bot.send_message(message.chat.id, message_text)
            await self.bot.send_message(message.chat.id, f"******************", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("🗞Важливі новини") or False