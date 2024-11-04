# Path para que funcione el TCL y TK de tkinter
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\Usuario\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Usuario\AppData\Local\Programs\Python\Python313\tcl\tk8.6'

# Librerías para que funcione el customtkinter
import customtkinter as ctk  # Asegúrate de haber instalado CustomTkinter con `pip install customtkinter`
# Tkinter normal para la versión inicial
from tkinter import *

# Librerias propias
# from focus_logic import focus

root = Tk()
root.title("Productivity App")
root.geometry("1280x720")  # Tamaño de la ventana

# Paneles
def paneles():
    # Panel principal que contiene los paneles izquierdo y derecho
    panel_main = Frame(root)
    panel_main.pack(fill=BOTH, expand=1)

    # Panel 1 Izquierdo con ancho fijo de 500 px
    panel_1 = Frame(panel_main, bg="#1a1e24", width=300)
    panel_1.pack(side=LEFT, fill=Y, padx=1, pady=1)
    panel_1.pack_propagate(False)  # Evita que el panel se ajuste automáticamente al contenido

    # Panel 2 Derecho que ocupa el resto del espacio disponible
    panel_2 = Frame(panel_main, bg="#060a12")
    panel_2.pack(side=RIGHT, fill=BOTH, expand=1, padx=1, pady=1)



    #funcion para limpiar panel 2
    def limpiar_panel_2():
        for widget in panel_2.winfo_children():
            widget.destroy()



    #Funciones de Botones
    def Focus_section():
        limpiar_panel_2() #limpia el panel_2 antes de cargar una nueva seccion.

        # Widgets de Modo Focus
        focus_label = Label(panel_2, text="Modo Focus", bg="#060a12", fg="white")
        focus_label.pack(pady=10)

        # Lista de procesos activos
        lista_procesos = ctk.CTkTextbox(panel_2, width=400, height=200)
        lista_procesos.pack(pady=10)

        # Control de tiempo de sesión
        tiempo_label = Label(panel_2, text="Duración de sesión (min):", bg="#060a12", fg="white")
        tiempo_label.pack()
        tiempo_entry = Entry(panel_2)
        tiempo_entry.pack(pady=5)

        # Botón para iniciar/terminar modo focus
        iniciar_button = Button(panel_2, text="Iniciar Modo Focus")
        iniciar_button.pack(pady=10)






    def Graficos_section():
        limpiar_panel_2() #limpia el panel_2 antes de cargar una nueva seccion.

        # Título de gráficos
        graficos_label = Label(panel_2, text="Gráficos de Uso", bg="#060a12", fg="white")
        graficos_label.pack(pady=10)

        # Área para mostrar gráficos
        cpu_label = Label(panel_2, text="CPU Usage", bg="#060a12", fg="white")
        cpu_label.pack()
        cpu_canvas = Canvas(panel_2, width=400, height=200)
        cpu_canvas.pack(pady=5)
        
        memory_label = Label(panel_2, text="Memory Usage", bg="#060a12", fg="white")
        memory_label.pack()
        memory_canvas = Canvas(panel_2, width=400, height=200)
        memory_canvas.pack(pady=5)


    def Configuracion_section():
        limpiar_panel_2() #limpia el panel_2 antes de cargar una nueva seccion.

        # Título de configuración
        configuracion_label = Label(panel_2, text="Configuración", bg="#060a12", fg="white")
        configuracion_label.pack(pady=10)

        # Lista de procesos permitidos
        permitidos_label = Label(panel_2, text="Procesos Permitidos", bg="#060a12", fg="white")
        permitidos_label.pack()
        lista_permitidos = ctk.CTkTextbox(panel_2, width=400, height=200)
        lista_permitidos.pack(pady=10)

        # Botones para editar lista de permitidos
        add_button = Button(panel_2, text="Agregar Proceso")
        add_button.pack(pady=5)
        remove_button = Button(panel_2, text="Quitar Proceso")
        remove_button.pack(pady=5)



    #Botones de Panel Izquierdo
    def botones_izquierda():
        #Creacion de Botones
        Focus_button = Button(panel_1, command= (Focus_section), text="Modo Focus", fg="white", font="Roboto", bg="#282e38", activebackground="#1a1e24", padx=100, pady=70)
        Graficos_button = Button(panel_1, command= (Graficos_section), text="Ver Gráficos", fg="white", font="Roboto", bg="#282e38", activebackground="#1a1e24", padx=100, pady=70)
        Configuracion_button = Button(panel_1, command= (Configuracion_section), text="Configuración", fg="white", font="Roboto", bg="#282e38", activebackground="#1a1e24", padx=100, pady=70)
        #Orden
        Focus_button.grid(row=1, column=0)
        Graficos_button.grid(row=2, column=0)
        Configuracion_button.grid(row=3, column=0)
    
    #Loop botones
    botones_izquierda()

#loop principales
root.resizable(False, False)  # Para que el usuario no pueda estirar la ventana
paneles()  # Llama a la función para crear los paneles
root.mainloop()  # Loop principal de la interfaz
