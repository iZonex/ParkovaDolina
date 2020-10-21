from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

class ContactsScreen(Screen):

    SECTIONS = [MAIN_MENU]

    TEXT_DATA = {
        "Контакт Строй Сіті Development": (
            "Строй Сіті Development\n"
            "Фактична адреса: Україна м.Київ, вул. Гончарна, 12\n"
            "Індекс: 01025\n"
            "Тел: +38(044)333-77-33\n"
            "Пошта: info@stroycity.com.ua\n"
            "Сайт: http://stroycity.com.ua\n"
        ),
        "Контакт Фінансова компанія ЖИТЛО-КАПІТАЛ": (
            'Фінансова компанія "ЖИТЛО-КАПІТАЛ"\n'
            "Юридична адреса: Київ, 33-Б, вул. Ярославів Вал\n"
            "Фактична адреса: Київ, вул. Протасів Яр, 2-Д, офіс 2\n"
            "ЄДРПОУ: 35393445\n"
            "Тел: +38(044)374-03-08\n"
            "Пошта: info@zhytlo.capital\n"
            "Сайт: https://z-capital.com.ua/\n"
        ),
    }

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def skip_context(self, text):
        if text.startswith("Контакт "):
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
            keyboard.add(types.KeyboardButton(text="↩️Назад"))
            await self.bot.send_message(message.chat.id, "Оберіть контакт.", reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        if message.text.startswith("Контакти") or message.text.startswith("Контакт"):
            return True
        return False