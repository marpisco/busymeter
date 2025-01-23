import asyncio
from bleak import BleakScanner
from operator import length_hint
import time
import os

async def main():
    os.system("cls")
    devices = await BleakScanner.discover()
    print(length_hint(devices))
    for d in devices:
        print(d)
    time.sleep(60)

while True:
    asyncio.run(main())