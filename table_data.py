from tkinter import *
from tkinter import ttk

class TableData(Frame):
    def __init__(self, master=None, student_data=None):
        super().__init__(master)
        self.master = master
        self.master.title("Dato del estudiante")
        self.pack()
        self.crear_tabla(student_data)

    def crear_tabla(self, student_data):

        columnas = ("Legajo", "DNI", "Nombre y Apellido", "Email", "Domicilio", "Fecha de Nacimiento", "Carrera", "Año de Ingreso")
        tabla = ttk.Treeview(self, columns=columnas, show="headings")


        for col in columnas:
            tabla.heading(col, text=col)


        tabla.column("Legajo", width=80)
        tabla.column("DNI", width=100)
        tabla.column("Nombre y Apellido", width=150)
        tabla.column("Email", width=150)
        tabla.column("Domicilio", width=150)
        tabla.column("Fecha de Nacimiento", width=150)
        tabla.column("Carrera", width=120)
        tabla.column("Año de Ingreso", width=100)


        if student_data:
            tabla.insert("", "end", values=student_data)


        tabla.pack(fill="both", expand=True)
