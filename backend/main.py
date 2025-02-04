## ------------------------------------
## BusyMeter alpha v0.1
## Backend - Programada por Marco Pisco <marco@marcopisco.com>
## ------------------------------------

import asyncio
from bleak import BleakScanner
from operator import length_hint
import time
import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

# Limpar o histórico dos dados passados
for _ in range(0, 60):
    file = open("api\\" + str(_), "w")
    file.write("0")
    file.close()

# Função principal
async def main():
    while True:
        devices = await BleakScanner.discover(timeout=15, scanning_mode='active')
        print("[INFO]: Descobriram-se" + length_hint(devices) + "dispositivos. A servir na API.")

        # Puxar ficheiros para a frente, por exemplo 0 passa a ser 1, 1 passa a ser 2, etc.
        for i in range(59, 0, -1):
            with open(f"api\\{i}", "w") as file:
                with open(f"api\\{i-1}", "r") as prev_file:
                    file.write(prev_file.read())

        with open("api\\0", "w") as file:
            file.write(str(length_hint(devices)))

        # Código repete-se a cada 30 segundso
        await asyncio.sleep(30)
        print("[INFO]: Scanner a dormir durante 30 segundos.")

# Definições do Servidor Básico HTTP do Python
class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def list_directory(self, path):
        self.send_error(404, "BusyMeter API alpha v0.1. Use /<intervalos> para receber os dados.")
        return None

    def translate_path(self, path):
        # Serve only the 'api' directory
        path = os.path.join(os.getcwd(), 'api', path.lstrip('/'))
        return path

# Thread do servidor
def thread_webserver():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    httpd.serve_forever()

# Definições thread
def webserver():
    server_thread = threading.Thread(target=webserver)
    server_thread.daemon = True
    server_thread.start()

# Funções a rodar no ficheiro.
if __name__ == "__main__":
    webserver()
    asyncio.run(main())