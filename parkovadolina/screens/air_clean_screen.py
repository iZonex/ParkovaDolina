import asyncio
import time
from parkovadolina.utils.weather import get_weather_info
from parkovadolina.utils.rad import get_rad_sensor_info
from parkovadolina.utils.sensors import get_air_sensor_info
from parkovadolina.core.screen import Screen
from aiogram.types.message import ParseMode

def format_wind_direction(wind_data):
    COMPASS_TRANSLATION_MAP = { 
        "N": "Північи",
        "NNE": "Північного східу",
        "NE": "Північного східу",
        "ENE": "Східу",
        "E": "Східу",
        "ESE": "Східу",
        "SE": "Південного східу",
        "SSE": "Південного східу",
        "S": "Південья",
        "SSW": "Південья",
        "SW": "Південного західу",
        "WSW": "Західу",
        "W": "Західу",
        "WNW": "Західу",
        "NW": "Північного західу",
        "NNW": "Північного західу"
    }

    wind_from = wind_data.get("from")
    if wind_from:
        wind_speed = wind_data["speed"]
        return f"З {COMPASS_TRANSLATION_MAP[wind_from]} із швидкістю {wind_speed:.0f} м/с"
    return "немає"

class AirCleanScreen(Screen):

    SENSOR_ID = "48"
    AIR_PORT = "UKKK"
    CACHE_TTL_LAG = 600

    def __init__(self, bot, dao):
        self.bot = bot
        self.dao = dao
        self.cache_ttl = self.CACHE_TTL_LAG
        self.last_cache = time.time()
        self.cached_data = []

    async def gether_data(self):
        tasks = [get_air_sensor_info(self.SENSOR_ID), get_rad_sensor_info(), get_weather_info(self.AIR_PORT)]
        return await asyncio.gather(*tasks)

    async def screen(self, message):
        if self.last_cache <= time.time():
            self.cached_data = await self.gether_data()
            self.last_cache = time.time() + self.CACHE_TTL_LAG
        if all(self.cached_data):
            sensor_data, rad_sensor_data, weather_data = self.cached_data
            text_body = (
                f'<b>За адресою Кайсарова 7/9</b>\n'
                f'наступні показники датчиків\n\n'
                f"🌤PM2.5: {sensor_data['particles']['pm1']:.2f} мкг/м3\n"
                f"🌤PM10: {sensor_data['particles']['pm10']:.2f} мкг/м3\n"
                f"🌤PM1: {sensor_data['particles']['pm25']:.2f} мкг/м3\n"
                f"💦Вологість: {sensor_data['weather']['humidity']:.0f} %\n"
                f"🌡Температура: {weather_data['temp']:.0f} °C\n"
                f"💧Точка роси: {weather_data['dewpt']:.0f} °C\n"
                f"💨Вітер: {format_wind_direction(weather_data['wind'])}\n"
                f"🩺Тиск: {weather_data['press']:.0f} мбар\n"
                f"☢Радиационной Фон: {rad_sensor_data} мкЗв/ч\n"
            )
        else:
            text_body = (
                f'<b>За адресою Кайсарова 7/9</b>\n'
                f'Датчики якості повітря не доступні\n\n'
            )
        await self.bot.send_message(message.chat.id, text_body, parse_mode=ParseMode.HTML)

    @staticmethod
    def match(message):
        return message.text.startswith("🌤Клімат") or False