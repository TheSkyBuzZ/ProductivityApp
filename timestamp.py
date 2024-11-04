import psutil
import time, datetime
import win32gui
import win32process
import json
import keyboard

# Funciones de guardado y borrado de procesos
def guardar_procesos(procesos_permitidos, archivo="procesos_permitidos.json"):
    with open(archivo, "w") as file:
        json.dump(procesos_permitidos, file)

def cargar_procesos(archivo="procesos_permitidos.json"):
    try:
        with open(archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Log de actividades usadas fuera de focus
def guardar_log(proceso, cpu, memoria, archivo="focus_log.txt"):
    with open(archivo, "a") as log_file:  # "a" para agregar en vez de sobreescribir
        log_file.write(f"{proceso}, CPU: {cpu}%, Memoria: {memoria}MB\n")

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
procesos_monitorizados = cargar_procesos()

while True:
    cargar = input("Desea añadir un proceso a la lista? (y) (n):").lower()
    if cargar == "y":
        monitorizar_proceso = input("Por favor, escribe el nombre del proceso a añadir a la lista: ")
        procesos_monitorizados.append(monitorizar_proceso)
        guardar_procesos(procesos_monitorizados)
    else:
        break

# Función para obtener el proceso activo
def get_active_window_process():
    manejo_ventana = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(manejo_ventana)
    return psutil.Process(pid)

# Función principal de modo focus
def modo_focus():
    while True:
        # Si se presiona la tecla 'q', se detiene el monitoreo
        if keyboard.is_pressed('q'):
            print("Modo Focus desactivado.")
            break

        try:
            proceso_activo = get_active_window_process()
            process_name = proceso_activo.name()
            cpu_usage = proceso_activo.cpu_percent(interval=1) / psutil.cpu_count()
            memory_inmb = proceso_activo.memory_info().rss / (1024 * 1024)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

            # Muestra en consola
            print(f"\r{timestamp} | Proceso: {process_name} | CPU: {cpu_usage:.2f}% | Memory: {memory_inmb:.2f} MB", end="")

            # Verificar si el usuario está en modo focus
            if process_name not in procesos_monitorizados:
                guardar_log(process_name, cpu_usage, memory_inmb)
                print(f"\n¡Mantente en focus! No estás usando los procesos permitidos.")
                print(f"Proceso: {process_name} | Hora: {timestamp}")
                time.sleep(2)  # Pausa cuando el usuario está fuera de focus
            else:
                time.sleep(1)  # Intervalo normal de monitoreo

        except psutil.NoSuchProcess:
            print("\nEl proceso terminó o no se encuentra.")
            time.sleep(1)

modo_focus()
