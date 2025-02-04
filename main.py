import asyncio
from bleak import BleakScanner
from operator import length_hint
import time
import os

os.remove("test.txt")
async def main():
    devices = await BleakScanner.discover(timeout=10,scanning_mode='active')
    for d in devices:
        print(d)
    print(length_hint(devices))
    time.sleep(30)

while True:
    asyncio.run(main())