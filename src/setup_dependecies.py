import subprocess
import sys

# Definir la función para instalar un paquete específico
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Leer el archivo requirements.txt y procesar cada línea
with open("../requirements.txt") as file:
    for line in file:
        # Instalar cada paquete listado en requirements.txt
        install(line.strip())
