from telebot import types

# get_actual_state_of_month == choiced_state. if less then actual state. Issues with building, If equail Normal, If more great

class BuildingScreen:

    SECTIONS = ["🚪Вихід"]

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
    }

    STATUS_MAP_SMALL = {
        "1": "✅",
        "2": "❌",
    }

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    def generate_states(self, states_list_ids):
        return "\n".join([f'- {self.STATUS_MAP_SMALL.get("2")} {self.BUILDING_STATUS_MAP.get(i)}' for i in states_list_ids])

    def screen(self, message):
        plans = self.dao.building_plan.get()
        for i in plans.values():
            text_states = self.generate_states(i.get_expected_state())
            text_body = (
                f'<strong>🏗{self.BUILDING_NUMBERS.get(i.title, "").upper()}</strong>\n\n'
                f'<strong>План будівництва на {i.get_date()}:</strong>\n'
                f"{text_states}\n\n"
                f'<strong>Статус будівництва: {self.STATUS_MAP["2"]}</strong>'
            )
            self.bot.send_message(message.chat.id, text_body, parse_mode='HTML')
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
        keyboard.add(types.KeyboardButton(text="🚪Вихід"))
        self.bot.send_message(message.chat.id, "Допомагай тримати ці дані актуальними", reply_markup=keyboard)

    @staticmethod
    def match(message):
        return message.text.startswith("🗓Будівництво") or False