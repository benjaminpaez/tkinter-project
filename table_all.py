from tkinter import *
from tkinter import ttk

class TableAll(Frame):
    def __init__(self, master=None, student_data=None):
        super().__init__(master)
        self.master = master
        self.master.title("Datos del Estudiante")
        self.pack(fill='both', expand=True)
        self.crear_tabla(student_data)

    def crear_tabla(self, student_data):
        # Definir las columnas de la tabla
        columnas = ("Legajo", "DNI", "Nombre y Apellido", "Email", "Domicilio", "Fecha de Nacimiento", "Carrera", "Año de Ingreso")
        tabla = ttk.Treeview(self, columns=columnas, show="headings")

        # Configurar los encabezados de las columnas
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=120, anchor='w')  # Ajustar el ancho y la alineación

        # Insertar los datos en la tabla
        if student_data:
            for student in student_data:
                tabla.insert("", "end", values=student)

        tabla.pack(fill="both", expand=True)


