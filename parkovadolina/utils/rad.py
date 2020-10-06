import json
import aiohttp
import pprint
import asyncio

async def get_rad_sensor_info():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://opyt.com.ua/monitoring/json/?m=2&q=tree") as resp:
            data = await resp.text()
            data = json.loads(data)
    try:
        return data[0]["children"][2]["v"]
    except KeyError:
        pass
    return None

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_rad_sensor_info())