from parkovadolina.models.building_constants import BUILDING_NUMBERS, STATUS_MAP
from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import EXIT
# get_actual_state_of_month == choiced_state. if less then actual state. Issues with building, If equail Normal, If more great

class BuildingMainScreen(Screen):

    SECTIONS = [EXIT]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        plans = self.dao.building_plan.get()
        BUILDING_SECTIONS = [i.title for i in plans.values()]
        return [types.KeyboardButton(i) for i in BUILDING_SECTIONS + self.SECTIONS]

    async def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        keyboard.add(*self.sections)
        building_statuses = self.dao.building_status_results.get_building_status()
        result_date = self.dao.building_status_results.get_date()
        text_result = " \n".join([f"- {BUILDING_NUMBERS[k]}: {STATUS_MAP[v]}" for k,v in building_statuses.items()])
        text_template = (
            f"<strong>На {result_date} статус будівництва:</strong> \n\n"
            f"{text_result}"
        )
        await self.bot.send_message(message.chat.id, text_template, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    def match_context(self, message):
        return message.text.startswith("↩️Назад")

    @staticmethod
    def match(message):
        return message.text.startswith("🏗Будівництво") or False