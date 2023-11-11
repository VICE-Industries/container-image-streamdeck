import asyncio
import os

from loguru import logger
from pyModbusTCP.client import ModbusClient
import requests

ADDRESS_LED = os.environ.get("ADDRESS_LED", "192.168.88.201")
ADDRESS_GATEWAY = os.environ.get("ADDRESS_GATEWAY", "192.168.88.20")

url_led = f"http://{ADDRESS_LED}/color"


async def sensor_a():
    state = True
    u1 = ModbusClient(host=ADDRESS_GATEWAY, unit_id=1, timeout=0.1)
    while True:
        r = u1.read_discrete_inputs(0, 1)
        if r and r[0] != state:
            logger.info(f"Sensor A = {r[0]}")
            state = r[0]

            if not state:
                logger.info("Color is now BLUE")
                requests.post(f"{url_led}?red=0&green=0&blue=255")
        await asyncio.sleep(0.1)


async def sensor_b():
    state = True
    u1 = ModbusClient(host=ADDRESS_GATEWAY, unit_id=1, timeout=0.1)
    while True:
        r = u1.read_discrete_inputs(1, 1)
        if r and r[0] != state:
            logger.info(f"Sensor B = {r[0]}")
            state = r[0]

            if not state:
                logger.info("Color is now GREEN")
                requests.post(f"{url_led}?red=0&green=255&blue=0")
        await asyncio.sleep(0.1)


async def sensor_c():
    state = True
    u1 = ModbusClient(host=ADDRESS_GATEWAY, unit_id=1, timeout=0.1)
    while True:
        r = u1.read_discrete_inputs(2, 1)
        if r and r[0] != state:
            logger.info(f"Sensor C = {r[0]}")
            state = r[0]

            if not state:
                logger.info("Color is now RED")
                requests.post(f"{url_led}?red=255&green=0&blue=0")
            else:
                logger.info("Color is now ORANGE")
                requests.post(f"{url_led}?red=255&green=165&blue=0")
        await asyncio.sleep(0.01)


async def main():
    await asyncio.gather(sensor_a(), sensor_b(), sensor_c())


if __name__ == "__main__":
    asyncio.run(main())
