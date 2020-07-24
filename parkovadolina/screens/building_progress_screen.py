from telebot import types
from core.constants import EXIT
# get_actual_state_of_month == choiced_state. if less then actual state. Issues with building, If equail Normal, If more great

class BuildingScreen:

    SECTIONS = [EXIT]

    BUILDING_STATUS_MAP = {
        "1": "Котлован",
        "2": "Палі",
        "3": "Фундамент",
        "4": "Монолітний залізобетнний каркас",
        "5": "Стіни, перегородки, покрівля",
        "6": "Внутрішнє оздоблення",
        "7": "Вікна, двері, ліфти",
        "8": "Фасад",
        "9": "Внутрішні інженері мережі",
        "10": "Благоустрій",
        "11": "Зовнішні інженерні мережі",
        "12": "Будивництво завершенно"
    }
    
    BUILDING_NUMBERS = {
        "1": "Будинок №1 Секція №1-3",
        "2": "Будинок №1 Секція №4-6",
        "3": "Будинок №1 Секція №7-9",
        "4": "Будинок №2 Секція №1",
        "5": "Будинок №2 Секція №2",
        "6": "Будинок №2 Секція №3",
        "7": "Будинок №2 Секція №4",
    }

    PREFIX = "Йде етап будівництва: "

    STATUS_MAP = {
        "1": "✅Будуватися за планом",
        "2": "❌Будівництво зупинено",
        "3": "❗️Будівництво призупинене"
    }

    STATUS_MAP_SMALL = {
        "done": "✅",
        "waiting": "❌",
        "3": "❗️",
        "inprogress": "▶️",
    }

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def generate_states(self, done_states, inprogress_states):
        states = ["waiting" for i in range(len(self.BUILDING_STATUS_MAP))]
        for i in done_states:
            states[i] = "done"
        for i in inprogress_states:
            states[i-1] = "inprogress"
        return "\n".join([f'- {self.STATUS_MAP_SMALL.get(e)} {self.BUILDING_STATUS_MAP.get(str(i))}' for i,e in enumerate(states, start=1)])

    def progress_bar(self, progress=4, max_progress=12):
        estimated_line = ["□" for _ in range(max_progress)]
        for i in range(progress):
            estimated_line[i] = "■"
        return "".join(estimated_line)

    def screen(self, message):
        plans = self.dao.building_plan.get()
        for i in plans.values():
            
            progress = [int(i) for i in i.get_expected_state()]
            done_progress = [int(i) for i in range(0, min(progress)-1)]
            progress_percent = round(min(progress) / 12 * 100, 2)
            text_states = self.generate_states(done_progress, progress)
            text_body = (
                f'<strong>🏗{self.BUILDING_NUMBERS.get(i.title, "").upper()}</strong>\n\n'
                f'<strong>План будівництва на {i.get_date()}:</strong>\n'
                f"{text_states}\n\n"
                f'<strong>|{self.progress_bar(min(progress), 12)}| {progress_percent}% [{min(progress)} з 12]</strong>'
            )
            self.bot.send_message(message.chat.id, text_body, parse_mode='HTML')
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text=EXIT))
        self.bot.send_message(message.chat.id, self.STATUS_MAP["3"], reply_markup=keyboard)

    @staticmethod
    def match(message):
        return message.text.startswith("🏗Будівництво") or False