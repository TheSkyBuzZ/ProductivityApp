#prueba de commit

# Librerías CustomTkinter y Tkinter
import customtkinter as ctk
from tkinter import *

# Inicialización de `CustomTkinter` y configuración de tema y color principal
ctk.set_appearance_mode("dark")  # Opción de apariencia "light", "dark", o "system"
ctk.set_default_color_theme("blue")  # Tema de color base para la aplicación

# Configuración de la ventana principal
root = ctk.CTk()
root.title("Productivity App")
root.geometry("1280x720")
root.resizable(False, False)

# Paneles
def paneles():
    # Panel principal que contiene los paneles izquierdo y derecho
    panel_main = ctk.CTkFrame(root)
    panel_main.pack(fill=BOTH, expand=True)

    # Panel Izquierdo con ancho fijo
    panel_1 = ctk.CTkFrame(panel_main, width=300, fg_color="#1a1e24")
    panel_1.pack(side=LEFT, fill=Y, padx=1, pady=1)
    panel_1.pack_propagate(False)

    # Panel Derecho que ocupa el resto del espacio disponible
    panel_2 = ctk.CTkFrame(panel_main, fg_color="#060a12")
    panel_2.pack(side=RIGHT, fill=BOTH, expand=True, padx=1, pady=1)

    # Función para limpiar panel derecho
    def limpiar_panel_2():
        for widget in panel_2.winfo_children():
            widget.destroy()

    # Funciones de cada sección
    def Focus_section():
        limpiar_panel_2()
        focus_label = ctk.CTkLabel(panel_2, text="Modo Focus", text_color="white", font=("Roboto", 16))
        focus_label.pack(pady=10)
        lista_procesos = ctk.CTkTextbox(panel_2, width=400, height=200)
        lista_procesos.pack(pady=10)
        tiempo_label = ctk.CTkLabel(panel_2, text="Duración de sesión (min):", text_color="white")
        tiempo_label.pack()
        tiempo_entry = ctk.CTkEntry(panel_2, width=200)
        tiempo_entry.pack(pady=5)
        iniciar_button = ctk.CTkButton(panel_2, text="Iniciar Modo Focus")
        iniciar_button.pack(pady=10)

    def Graficos_section():
        limpiar_panel_2()
        graficos_label = ctk.CTkLabel(panel_2, text="Gráficos de Uso", text_color="white", font=("Roboto", 16))
        graficos_label.pack(pady=10)
        cpu_label = ctk.CTkLabel(panel_2, text="CPU Usage", text_color="white")
        cpu_label.pack()
        cpu_canvas = ctk.CTkCanvas(panel_2, width=400, height=200)
        cpu_canvas.pack(pady=5)
        memory_label = ctk.CTkLabel(panel_2, text="Memory Usage", text_color="white")
        memory_label.pack()
        memory_canvas = ctk.CTkCanvas(panel_2, width=400, height=200)
        memory_canvas.pack(pady=5)

    def Configuracion_section():
        limpiar_panel_2()
        configuracion_label = ctk.CTkLabel(panel_2, text="Configuración", text_color="white", font=("Roboto", 16))
        configuracion_label.pack(pady=10)
        permitidos_label = ctk.CTkLabel(panel_2, text="Procesos Permitidos", text_color="white")
        permitidos_label.pack()
        lista_permitidos = ctk.CTkTextbox(panel_2, width=400, height=200)
        lista_permitidos.pack(pady=10)
        add_button = ctk.CTkButton(panel_2, text="Agregar Proceso")
        add_button.pack(pady=5)
        remove_button = ctk.CTkButton(panel_2, text="Quitar Proceso")
        remove_button.pack(pady=5)

    # Botones en el Panel Izquierdo
    def botones_izquierda():
        Focus_button = ctk.CTkButton(panel_1, command=Focus_section, text="Modo Focus", 
                                     fg_color="#282e38", hover_color="#1a1e24", text_color="white", font=("Roboto", 16),
                                     width=250, height=70)
        Graficos_button = ctk.CTkButton(panel_1, command=Graficos_section, text="Ver Gráficos", 
                                        fg_color="#282e38", hover_color="#1a1e24", text_color="white", font=("Roboto", 16),
                                        width=250, height=70)
        Configuracion_button = ctk.CTkButton(panel_1, command=Configuracion_section, text="Configuración", 
                                             fg_color="#282e38", hover_color="#1a1e24", text_color="white", font=("Roboto", 16),
                                             width=250, height=70)
        # Posicionamiento
        Focus_button.pack(pady=20)
        Graficos_button.pack(pady=20)
        Configuracion_button.pack(pady=20)
    
    # Inicializa botones en el panel izquierdo
    botones_izquierda()

# Ejecuta función para crear paneles y loop principal
paneles()
root.mainloop()
