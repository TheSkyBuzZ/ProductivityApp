import psutil
import time
import datetime
import win32gui
import win32process
import json

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

def inicio_app():
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
    
    print(type(procesos_unicos))
    procesos_str = ""
    
    for proceso in procesos_unicos:
        procesos_str += f"- {proceso}\n"

    # Imprimir el string para depuración
    print(procesos_str)
    return procesos_str
