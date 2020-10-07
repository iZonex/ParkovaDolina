from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class ServicesScreen(Screen):


    LINK = "https://docs.google.com/spreadsheets/d/1-e1zIHAdkUViuqIhbNTJRKtOd0ja6PjCSawMxnvVSu4/edit?usp=sharing"

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao

    async def screen(self, message):
        text_body = (
            f'<b>Додати або подивитися послуги знижки та інше можна за цим посиланням:</b>\n\n'
            f'<a href="{self.LINK}">список послуг</a>'
        )
        await self.bot.send_message(message.chat.id, text_body, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("💸Послуги") or False