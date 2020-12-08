from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

# https://www.youtube.com/watch?v=9tXrfDh81cs&list=PLtEFikqmzOmjMD_rJFK5mjmVoF_j54Ixp&index=4
class CameraScreen(Screen):

    SECTIONS = [MAIN_MENU]

    TEXT_DATA = {
        "📹Камера Будинок 1 (вид з двору)": "https://www.youtube.com/watch?v=vz9AB4XhDvw \n",
        "📹Камера Вид з вул. Кайсарова": "https://www.youtube.com/watch?v=93dhtbJokjY \n",
        "📹Камера Вид на 6-9 секції з двору": "https://www.youtube.com/watch?v=DMXKCFIR8sw \n",
        "📹Камера Будинок 2": "https://www.youtube.com/watch?v=9tXrfDh81cs \n",
    }

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    def skip_context(self, text):
        if text.startswith("📹Камера"):
            return True
        return False

    async def screen(self, message):
        text_body = self.TEXT_DATA.get(message.text, None)
        if text_body:
            await self.bot.send_message(message.chat.id, text_body, parse_mode=ParseMode.HTML)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            for i in self.TEXT_DATA.keys():
                keyboard.add(types.KeyboardButton(text=i))
            keyboard.add(types.KeyboardButton(text=MAIN_MENU))
            await self.bot.send_message(message.chat.id, "Оберіть камеру.", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        if message.text.startswith("📹Камери") or message.text.startswith("📹Камера"):
            return True
        return False