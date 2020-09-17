import aiohttp
import pprint
import asyncio

URL = "https://misto.lun.ua/api/v1/sensors/now"

async def get_air_sensor_info():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://misto.lun.ua/api/v1/sensors/now") as resp:
            data = await resp.json()
    for i in data:
        if i['station']['name'] == '49':
            result = {
                "station": i['station'],
                "particles": i['particles'][0],
                "timestamp": i['timestamp'],
                "weather": i['weather'][0]
            }
            return result
    return None

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_sensor_info())