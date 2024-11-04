import psutil
import os
import time
import win32gui
import win32process

#Pedirle al usuario que inicialize los procesos a trabajar.
while True:
    print("----Inicia porfavor los procesos con los que vas a trabajar----")
    eleccion = input("Apreta Y para continuar: ").lower()

    if eleccion == "y":
        break
    else:
        print("Por favor, ingresa 'y' para continuar.")

print("")
print("Estos son los procesos disponibles:")
print("")

#Registrar procesos abiertos.
procesos_unicos = set()

for process in psutil.process_iter(["name", "exe"]):
    try:
        #obtener nombre y ruta del proceso
        nombre_proceso = process.info["name"]
        ruta_proceso = process.info["exe"]

        #Filtrar procesos sin nombre o ruta, para que pasen sin errores.
        if not nombre_proceso or not ruta_proceso:
            continue

        #Filtrar los procesos del Sistema que la ruta contenga "Windows".
        if "Windows" not in ruta_proceso:
            #Añadir al conjunto solo si no está duplicado.
            procesos_unicos.add(nombre_proceso)
    
    #Ignorar procesos que terminen esporádicamente antes de acceder a su informacion.
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        continue

for proceso in procesos_unicos:
    print(f"Proceso activo: {proceso}")

#Elegir proceso a monitorear:

print("")
monitorizar_proceso1 = input("Porfavor escriba el nombre del proceso °1 a monitorear: ")


def get_active_window_process():
    # Obtiene el handle de la ventana activa
    manejo_ventana = win32gui.GetForegroundWindow()
    # Obtiene el PID del proceso que está en la ventana activa
    _, pid = win32process.GetWindowThreadProcessId(manejo_ventana)
    # Usa el PID para obtener el proceso con psutil
    proceso__activo = psutil.Process(pid)
    return proceso__activo

while True:
    try:
        # Obtenemos el proceso de la ventana activa
        proceso_ = get_active_window_process()
        
        # Nombre del proceso y uso de recursos
        process_name = proceso_.name()
        cpu_usage = proceso_.cpu_percent(interval=1) / psutil.cpu_count()
        memory_inmb = proceso_.memory_info().rss / (1024 * 1024)
        
        while True:
            # Muestra en consola
            print(f"\rVentana activa: {process_name} | CPU: {cpu_usage:.2f}% | Memory: {memory_inmb:.2f} MB")

            #verificar que el usuario no se haya salido de focus.
            if process_name == monitorizar_proceso1:
                break
            else:
                print("Mantente en focus!")

    except psutil.NoSuchProcess:
        # En caso de que el proceso termine antes de acceder a él
        print("El proceso terminó o no se encuentra.")
    
    time.sleep(1)  # Espera un segundo antes de volver a verificar

