import asyncio
from bleak import BleakScanner
from operator import length_hint
import time
import os

async def main():
    os.system("cls")
    devices = await BleakScanner.discover(timeout=15,scanning_mode='active')
    for d in devices:
        print(d)
    print(length_hint(devices))
    print("Esperar")
    time.sleep(30)

while True:
    asyncio.run(main())