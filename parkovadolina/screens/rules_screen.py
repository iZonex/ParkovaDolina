from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class RulesScreen(Screen):

    SECTIONS = [MAIN_MENU]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def rules_confirm(self, message):
        user_id = message.from_user.id
        self.dao.users.create(user_id)
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Головне меню"))
        await self.bot.send_message(message.chat.id, "Дякую за те що прийняли правила", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    async def rules_chats(self, message):
        text_body = "📋 Правила чату:\n\n"
        text_body += "".join(self.dao.rules.get())
        available_options = ["🤝Згоден з правилами"]
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        [ keyboard.add(types.KeyboardButton(text=i)) for i in available_options]
        keyboard.add(types.KeyboardButton(text=MAIN_MENU))
        await self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    async def screen(self, message):
        if message.text.startswith("🤝Згоден з правилами"):
            await self.rules_confirm(message)
        else:
            await self.rules_chats(message)

    @staticmethod
    def match(message):
        if message.text.startswith("🤝Згоден з правилами") or message.text.startswith("📋Правила"):
            return True
        return False