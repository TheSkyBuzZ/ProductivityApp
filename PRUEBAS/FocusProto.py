import psutil
import os
import time
import win32gui
import win32process

# Pedirle al usuario que inicialice los procesos
while True:
    print("----Inicia por favor los procesos con los que vas a trabajar----")
    eleccion = input("Presiona 'Y' para continuar: ").lower()
    if eleccion == "y":
        break
    else:
        print("Por favor, ingresa 'y' para continuar.")

print("\nEstos son los procesos disponibles:\n")

# Registrar procesos únicos abiertos
procesos_unicos = set()

for process in psutil.process_iter(["name", "exe"]):
    try:
        nombre_proceso = process.info["name"]
        ruta_proceso = process.info["exe"]
        if nombre_proceso and ruta_proceso and "Windows" not in ruta_proceso:
            procesos_unicos.add(nombre_proceso)
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

# Mostrar los procesos disponibles al usuario
for proceso in procesos_unicos:
    print(f"Proceso activo: {proceso}")

# Elegir procesos a monitorear
print("")
procesos_monitorizados = []
monitorizar_proceso1 = input("Por favor, escribe el nombre del proceso °1 a monitorear: ")
procesos_monitorizados.append(monitorizar_proceso1)

# Función para obtener el proceso activo
def get_active_window_process():
    manejo_ventana = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(manejo_ventana)
    return psutil.Process(pid)

while True:
    try:
        proceso_activo = get_active_window_process()
        process_name = proceso_activo.name()
        cpu_usage = proceso_activo.cpu_percent(interval=1) / psutil.cpu_count()
        memory_inmb = proceso_activo.memory_info().rss / (1024 * 1024)

        # Muestra en consola (sobreescribiendo la misma línea)
        print(f"\rVentana activa: {process_name} | CPU: {cpu_usage:.2f}% | Memory: {memory_inmb:.2f} MB", end="")

        # Verificar si el usuario está en modo focus
        if process_name not in procesos_monitorizados:
            print("\n¡Mantente en focus! No estás usando los procesos permitidos.")
            print("!!!")
            time.sleep(2)  # Espera unos segundos antes de verificar de nuevo
        else:
            time.sleep(1)  # Intervalo normal de monitoreo

    except psutil.NoSuchProcess:
        print("\nEl proceso terminó o no se encuentra.")
        time.sleep(1)
