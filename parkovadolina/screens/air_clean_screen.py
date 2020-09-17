from parkovadolina.utils.sensors import get_air_sensor_info
from parkovadolina.core.screen import Screen
from aiogram import types
from aiogram.types.message import ParseMode
from parkovadolina.core.constants import MAIN_MENU

# {'particles': {'pm1': 9.9,
#                'pm10': 10.9,
#                'pm25': 15.5,
#                'timestamp': '2020-09-17T12:50:00Z'},
#  'station': {'coordinates': {'lat': 30.4678111, 'lng': 50.3960801},
#              'name': '49'},
#  'timestamp': '2020-09-17T12:50:00Z',
#  'weather': {'humidity': 39.48701555302285,
#              'pressure': 98793.39476351772,
#              'temperature': 28.38482402977713,
#              'timestamp': '2020-09-17T12:50:00Z'}}

class AirCleanScreen(Screen):

    SECTIONS = [MAIN_MENU]

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.sections = self._build_sections()

    def _build_sections(self):
        return [types.KeyboardButton(i) for i in self.SECTIONS]

    async def screen(self, message):
        data = await get_air_sensor_info()
        text_body = (
            f'<b>За адресою Кайсарова 7/9</b>\n'
            f'наступні показники датчиків якості повітря\n\n'
            f"🌤PM2.5: {data['particles']['pm1']:.2f} мкг/м3\n"
            f"🌤PM10: {data['particles']['pm10']:.2f} мкг/м3\n"
            f"🌤PM1: {data['particles']['pm25']:.2f} мкг/м3\n"
            f"💦Вологість: {data['weather']['humidity']:.0f} %\n"
            f"🌡Температура: {data['weather']['temperature']:.0f} °C\n"

        )
        keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        keyboard.add(types.KeyboardButton(text=MAIN_MENU))
        await self.bot.send_message(message.chat.id, text_body, reply_markup=keyboard, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("🌤Чистота повітря") or False