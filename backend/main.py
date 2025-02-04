import asyncio
from bleak import BleakScanner
from operator import length_hint
import time
import os

for _ in range (0, 60):
    # import a library for files and create a file
    import os
    # open a file in write mode
    file = open("api\\" + str(_), "w")
    # write to the file
    file.write("0")
    # close the file
    file.close()

async def main():
    devices = await BleakScanner.discover(timeout=10, scanning_mode='active')
    for d in devices:
        print(d)
    print(length_hint(devices))

    # Shift the contents of the files
    for i in range(59, 0, -1):
        with open(f"api\\{i}", "w") as file:
            with open(f"api\\{i-1}", "r") as prev_file:
                file.write(prev_file.read())

    # Write new data to file 0
    with open("api\\0", "w") as file:
        file.write(str(length_hint(devices)))

    await asyncio.sleep(30)

def webserver():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

webserver()
while True:
    asyncio.run(main())