from telebot import types
from core.constants import EXIT
# get_actual_state_of_month == choiced_state. if less then actual state. Issues with building, If equail Normal, If more great

class BuildingMainScreen:

    SECTIONS = [EXIT]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        plans = self.dao.building_plan.get()
        BUILDING_SECTIONS = [i.title for i in plans.values()]
        return [types.KeyboardButton(i) for i in BUILDING_SECTIONS + self.SECTIONS]

    def screen(self, message):
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=1)
        keyboard.add(*self.sections)
        self.bot.send_message(message.chat.id, "Оберить будинок", reply_markup=keyboard)

    @staticmethod
    def match(message):
        return message.text.startswith("🏗Будівництво") or False