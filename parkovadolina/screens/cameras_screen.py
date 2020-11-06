from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class CameraScreen(Screen):

    SECTIONS = [MAIN_MENU]

    TEXT_DATA = {
        "📹Камера 1": "https://www.youtube.com/watch?v=MlYr5_WSM40 \n",
        "📹Камера 2": "https://www.youtube.com/watch?v=93dhtbJokjY \n",
        "📹Камера 3": "https://www.youtube.com/watch?v=12jFkDH1fu0 \n",
        "📹Камера 4": "https://www.youtube.com/watch?v=M6UtPg4mjgk \n",
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