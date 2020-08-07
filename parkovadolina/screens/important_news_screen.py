from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types import ParseMode
from datetime import datetime
from parkovadolina.core.constants import EXIT

class ImportantNewsScreen(Screen):

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def in_line(self, query):
        news_list = self.dao.important_news.get()[::-1]
        page_index = int(query.data.split("_")[2])
        try:
            news = news_list[page_index]
        except IndexError:
            news = news_list[-1]
        keyboard_markup = types.InlineKeyboardMarkup(row_width=2)
        row_btns = []
        if not page_index - 1 < 0:
            row_btns.append(
                types.InlineKeyboardButton('<< Попередня', callback_data=f'news_prev_{page_index-1}')
            )
        if page_index + 1 <= len(news_list):
            row_btns.append(
                types.InlineKeyboardButton('Наступня >>', callback_data=f'news_next_{page_index+1}')
            )
       
        keyboard_markup.row(*row_btns)
        date = datetime.fromtimestamp(int(news.date)).strftime('%Y-%m-%d %H:%M:%S')
        message_text = (
            f"{news.text}\n"
            f"{date} - @{news.username}"
        )

        await self.bot.edit_message_text(message_text, chat_id=query.message.chat.id, message_id=query.message.message_id, reply_markup=keyboard_markup, parse_mode=ParseMode.HTML)

    async def screen(self, message):
        news_list = self.dao.important_news.get()
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text=EXIT))
        
        if not news_list:
            await self.bot.send_message(message.chat.id, "Вибачте поки немає важливих новин.", reply_markup=keyboard, parse_mode=ParseMode.HTML)
        else:
            await self.bot.send_message(message.chat.id, "<b>Новини за тиждень:</b>\n\n", reply_markup=keyboard, parse_mode=ParseMode.HTML)
            keyboard_markup = types.InlineKeyboardMarkup(row_width=2)

            text_and_data = (
                ('Наступня >>', 'news_next_1'),
                
            )

            row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
            keyboard_markup.row(*row_btns)
            news = news_list[::-1][0]
            date = datetime.fromtimestamp(int(news.date)).strftime('%Y-%m-%d %H:%M:%S')
            message_text = (
                f"{news.text}\n"
                f"{date} - @{news.username}"
            )

            await self.bot.send_message(message.chat.id, message_text, reply_markup=keyboard_markup, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("🗞Важливі новини") or False

    @staticmethod
    def in_line_match_pattern(query):
        if query.data.startswith("news_"):
            return True
        return False