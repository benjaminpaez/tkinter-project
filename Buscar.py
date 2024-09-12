from tkinter import *
from Listado import Listado
from table_data import TableData
from table_all import TableAll
from db_interactions import HandlerDB


class Buscar(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=None)
        self.master = master
        self.pack()
        self.configure(bg="#183c54")
        self.crear_widgets()
        self.gestion_estudiantes = HandlerDB()

    def crear_widgets(self):
        self.campos = ("Arial", 10)
        self.titulo = ("Arial", 16, "bold")
        self.botones = ("Tahoma", 9)
        self.colorBotones = "#183c54"

        self.titulo = Label(self, text="BIENVENIDOS A \n GESTION DE ESTUDIANTES", justify='center', fg="#FFFFFF",
                            bg="#183c54", font=self.titulo)
        self.titulo.grid(row=0, column=0, columnspan=4, pady=50)

        self.Legajo = Label(self, text="Legajo:", anchor="w", justify="left", bg="#183c54", fg="#FFFFFF",
                            font=self.campos)
        self.Legajo.grid(row=1, column=0, padx=15, sticky="w")

        self.borde_color = Frame(self, bg="#FFFFFF", padx=1, pady=1)
        self.borde_color.grid(row=2, column=0, columnspan=4, padx=15, pady=8, sticky="ew")
        self.cuadro_Legajo = Entry(self.borde_color, bg="#183c54")
        self.cuadro_Legajo.pack(fill="both", expand=True)
        self.cuadro_Legajo.config(fg="#F0F8FF", justify="center", font="arial, 9")

        self.Dni = Label(self, text="Dni:", anchor="w", justify="left", bg="#183c54", fg="#FFFFFF", font=self.campos)
        self.Dni.grid(row=3, column=0, padx=15, sticky="w")

        self.borde_color2 = Frame(self, bg="#FFFFFF", padx=1, pady=1)
        self.borde_color2.grid(row=4, column=0, columnspan=4, padx=15, pady=8, sticky="ew")
        self.cuadro_Dni = Entry(self.borde_color2, bg="#183c54")
        self.cuadro_Dni.pack(fill="both", expand=True)
        self.cuadro_Dni.config(fg="#F0F8FF", justify="center", font="arial, 9")

        self.BotonAgregar = Button(self, text="Agregar", bg="#6c757d", fg="#FFFFFF", font=self.botones,
                                   command=self.abrir_agregar)
        self.BotonAgregar.grid(row=5, column=0, padx=20, pady=30, sticky="ew")

        self.BotonBuscar = Button(self, text="Buscar",bg="#28a745", font=self.botones, fg="#FFFFFF",
                                  command=self.search_student)
        self.BotonBuscar.grid(row=5, column=3, padx=20, pady=30, sticky="ew")

        self.BotonMostrarTodos = Button(self, text="Mostrar Todos", bg="#FFFFFF", font=self.botones,
                                        fg=self.colorBotones,
                                        command=self.show_all_students)
        self.BotonMostrarTodos.grid(row=5, column=2, padx=20, pady=30, sticky="ew")

    def abrir_agregar(self):
        ventana_agregar = Toplevel(self.master)
        ventana_agregar.geometry("550x300")
        ventana_agregar.resizable(False, False)
        Listado(ventana_agregar)

    def search_student(self):
        legajo = self.cuadro_Legajo.get()
        dni = self.cuadro_Dni.get()

        student = self.gestion_estudiantes.get_data_student(legajo, dni)
        if student:
            result = Toplevel(self.master)
            TableData(result, student)

    def show_all_students(self):
        students = self.gestion_estudiantes.show_students()
        print(students)
        if students:
            result = Toplevel(self.master)
            TableAll(result, students)
