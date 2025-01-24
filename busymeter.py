import bluetooth
import time
import os

def lookup():
    nearby_devices = bluetooth.discover_devices()
    os.system('cls')
    print("Found {} devices.".format(len(nearby_devices)))

    for addr in nearby_devices:
        print("  {}".format(addr))

while True:
    lookup()
    time.sleep(60)