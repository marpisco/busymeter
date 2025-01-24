import asyncio
from bleak import BleakScanner
from operator import length_hint
import time
import os

async def main():
    os.system("cls")
    devices = await BleakScanner.discover(timeout=8,scanning_mode='active')
    print(length_hint(devices))
    for d in devices:
        print(d)
    print("Esperar 65 segundos para voltar a dar scan")
    time.sleep(65)

while True:
    asyncio.run(main())