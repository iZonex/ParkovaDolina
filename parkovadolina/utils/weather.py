import aiohttp
import asyncio
from metar import Metar

async def get_weather_info(station="UKKK"):
    obj = {
        "wind": {"from": None, "to": None, "speed": 0},
        "temp": 0,
        "dewpt": 0
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{station.upper()}.TXT") as resp:
            data = await resp.text()
            for i in data.split('\n'):
                if i.startswith(station.upper()):
                    obs = Metar.Metar(i)   
                    obj = {
                        "wind": {
                            "from": obs.wind_dir_from.compass() if obs.wind_dir_from else None,
                            "to": obs.wind_dir_to.compass() if obs.wind_dir_to else None,
                            "speed": obs.wind_speed.value('MPS')
                        },
                        "temp": obs.temp.value("C"),
                        "dewpt": obs.dewpt.value("C"),
                        "press": obs.press.value("MB")
                    }
    return obj


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_weather_info())