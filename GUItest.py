#path para que funcione el tcl y tk de tkinter
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\Usuario\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Usuario\AppData\Local\Programs\Python\Python313\tcl\tk8.6'
#librerias para que funcione el customtkinter
import customtkinter as ctk  # Asegúrate de haber instalado CustomTkinter con `pip install customtkinter`
import json
import threading  # Para ejecutar el modo focus sin bloquear la interfaz

# Configuración inicial de la ventana
def iniciar_interfaz():
    # Configuración de la ventana principal
    root = ctk.CTk() 
    root.title("Modo Focus")
    root.geometry("600x400")  # Ajusta el tamaño de la ventana

    # **Sección 1: Lista de Procesos Permitidos**
    # -------------------------------
    lista_procesos = ctk.CTkTextbox(root, width=200, height=200)  # Listbox para mostrar procesos permitidos
    lista_procesos.pack(pady=20)

    # Cargar procesos desde el archivo y mostrarlos en el textbox
    def cargar_procesos(archivo="procesos_permitidos.json"):
        try:
            with open(archivo, "r") as file:
                procesos = json.load(file)
                contenido = "\n".join(procesos)  # Convierte la lista de procesos en un solo string con saltos de línea
                lista_procesos.configure(state="normal")  # Habilita el textbox para modificar el contenido
                lista_procesos.delete("0.0", "end")  # Usa delete desde la posición inicial hasta el final
                lista_procesos.insert("0.0", contenido)  # Inserta el contenido como un string en una sola operación
                lista_procesos.configure(state="disabled")  # Deshabilita el textbox para evitar ediciones
        except FileNotFoundError:
            print("No se encontró el archivo de procesos permitidos.")
    
    cargar_procesos()  # Llama a la función para cargar procesos al iniciar

    # Botón para actualizar lista de procesos permitidos
    actualizar_btn = ctk.CTkButton(root, text="Actualizar Procesos", command=cargar_procesos)
    actualizar_btn.pack(pady=10)

    # **Sección 2: Botón para iniciar/detener el modo focus**
    # -------------------------------
    modo_focus_activo = False

    def iniciar_modo_focus():
        print("Modo Focus iniciado")


    # Esta función se usará para alternar el estado del modo focus
    def alternar_modo_focus():
        nonlocal modo_focus_activo
        modo_focus_activo = not modo_focus_activo

        if modo_focus_activo:
            iniciar_modo_focus()  # Ejecuta el monitoreo en un hilo separado para no congelar la interfaz
            modo_btn.configure(text="Detener Modo Focus")
        else:
            # Aquí deberías agregar lógica para detener el monitoreo
            modo_btn.configure(text="Iniciar Modo Focus")
            # Tal vez podrías detener el hilo o cambiar el valor de una variable de control

    # Botón para iniciar y detener el modo focus
    modo_btn = ctk.CTkButton(root, text="Iniciar Modo Focus", command=alternar_modo_focus)
    modo_btn.pack(pady=10)

    # **Sección 3: Indicador de estado (focus/no focus)**
    # -------------------------------
    estado_label = ctk.CTkLabel(root, text="Estado: Fuera de Focus", text_color="red")
    estado_label.pack(pady=20)

    # Actualizar el estado de focus en el GUI
    def actualizar_estado(en_focus):
        if en_focus:
            estado_label.configure(text="Estado: En Focus", text_color="green")
        else:
            estado_label.configure(text="Estado: Fuera de Focus", text_color="red")

    # Ejecuta el bucle de la interfaz
    root.mainloop()

# Llama a la función para iniciar la interfaz gráfica
iniciar_interfaz()
