import tkinter as tk
from tkinter import ttk

def crearTabla(parent):
    frame_tabla = tk.Frame(parent)
    frame_tabla.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    # Etiqueta 
    tk.Label(frame_tabla, text="Lista de Alumnos", justify='center', width=80, fg="blue").grid(row=0, column=0, pady=1)

    # Definir las columnas de la tabla
    columnas = ("Legajo", "DNI", "Apellido y Nombre", "Email", "Domicilio", "Fecha de Nacimiento", "Carrera", "Fecha de Ingreso")
     
    # Crear el Treeview
    tree = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=120)

    # Agregar el Treeview al frame
    tree.grid(row=1, column=0, sticky="nsew")
    
    return frame_tabla

    
   
