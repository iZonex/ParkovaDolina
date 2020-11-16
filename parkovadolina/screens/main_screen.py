from parkovadolina.core.screen import Screen
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import EXIT, MAIN_MENU
from aiogram import types


class MainScreen(Screen):

    WELCOME_TEXT = "Вітання! Я буду тобі допомагати протягом усього спілкування в групі інвесторів ЖК Голосіївська Долина"
    RULES_NOTICE = "Прошу ознайомитися з правилами. Натисніть знизу кнопку 📋Правила для продовження"
    SECTIONS = ["🗞Важливі новини", "🎖Iніціативна група", "🏗Будівництво", "💸Послуги",
                # "🧩Персони", 
                "👂Комунікація",
                "🌤Клімат",
                #"🗓Активності",
                #"🔍Відповіді на запитання",
                "📹Камери",
                "🤝Група підтверджених інвесторів"]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        user = self.dao.users.get_by_user_id(message.from_user.id)
        if user:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            keyboard.add(*self.sections)
            if message.text == "/start":
                await self.bot.send_message(message.chat.id, self.WELCOME_TEXT, reply_markup=keyboard, parse_mode=ParseMode.HTML)
            else:
                await self.bot.send_message(message.chat.id, "Головне меню", reply_markup=keyboard, parse_mode=ParseMode.HTML)
        else:
            keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            keyboard.add(types.KeyboardButton(text="📋Правила"))
            await self.bot.send_message(message.chat.id, f"{self.WELCOME_TEXT}\n\n{self.RULES_NOTICE}", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        if message.text.startswith("Головне меню") or message.text.startswith(MAIN_MENU) or message.text.startswith(EXIT) or message.text.startswith("❇️ Головне меню") or message.text.startswith("/start"):
            return True
        return False
