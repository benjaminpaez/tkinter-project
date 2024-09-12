from tkinter import *
import tkinter as tk
from db_interactions import HandlerDB


def convEnt(entry_string, string):
    entry_str = entry_string.get()
    try:
        integer = int(entry_str)
        return integer
    except ValueError:
        print(f"Error: el valor ingresado en {string} no es un numero entero")
        return None


class Listado(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Agregar estudiante")
        self.master.geometry("300x445")
        self.pack(fill=BOTH, expand=True)
        self.configure(bg="#183c54")
        self.crear_listado()
        self.gestion_estudiantes = HandlerDB()

    def clear_fields(self, *args):
        for arg in args:
            if arg is not None:
                arg.delete(0, tk.END)

    def guardar_estudiante(self):

        legajo = convEnt(self.entry_legajo, "Legajo")
        dni = convEnt(self.entry_dni, "DNI")
        nombre_apellido = self.entry_nombre_apellido.get()
        nacimiento = self.entry_nacimiento.get()
        domicilio = self.entry_domicilio.get()
        email = self.entry_email.get()
        carrera = self.entry_carrera.get()
        ingreso = convEnt(self.entry_ingreso, "Ingreso")

        self.gestion_estudiantes.create_students(legajo, dni, nombre_apellido, email, domicilio, nacimiento, carrera,
                                                 ingreso)
        self.clear_fields(self.entry_legajo, self.entry_dni, self.entry_nombre_apellido,
                          self.entry_nacimiento, self.entry_domicilio, self.entry_email,
                          self.entry_carrera, self.entry_ingreso)

    def crear_listado(self):
        campos = ("Arial", 10)
        fondo = "#183c54"
        texto = "#FFFFFF"
        botones = ("Tahoma", 9)
        colorBotones = "#183c54"

        Label(self, text="Legajo:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=0, column=0, padx=20,
                                                                                          pady=1, sticky="w")
        self.borde_color = Frame(self, bg="#FFFFFF", padx=1, pady=1)
        self.borde_color.grid(row=1, column=0, padx=20, pady=2)
        self.entry_legajo = Entry(self.borde_color, bg="#183c54", width=30)
        self.entry_legajo.pack(fill="both", expand=True)
        self.entry_legajo.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="DNI:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=2, column=0, padx=20, pady=1,
                                                                                       sticky="w")
        self.entry_dni = Entry(self, bg="#183c54", width=30)
        self.entry_dni.grid(row=3, column=0, padx=20, pady=2)
        self.entry_dni.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="Nombre y Apellido:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=4, column=0,
                                                                                                     padx=20, pady=1,
                                                                                                     sticky="w")
        self.entry_nombre_apellido = Entry(self, bg="#183c54", width=30)
        self.entry_nombre_apellido.grid(row=5, column=0, padx=20, pady=2)
        self.entry_nombre_apellido.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="Nacimiento (YYYY-MM-DD):", justify="left", bg=fondo, fg=texto, font=campos).grid(row=6,
                                                                                                           column=0,
                                                                                                           padx=20,
                                                                                                           pady=1,
                                                                                                           sticky="w")
        self.entry_nacimiento = Entry(self, bg="#183c54", width=30)
        self.entry_nacimiento.grid(row=7, column=0, padx=20, pady=2)
        self.entry_nacimiento.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="Domicilio:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=8, column=0, padx=20,
                                                                                            pady=1, sticky="w")
        self.entry_domicilio = Entry(self, bg="#183c54", width=30)
        self.entry_domicilio.grid(row=9, column=0, padx=20, pady=2)
        self.entry_domicilio.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="Email:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=10, column=0, padx=20,
                                                                                         pady=1, sticky="w")
        self.entry_email = Entry(self, bg="#183c54", width=30)
        self.entry_email.grid(row=11, column=0, padx=20, pady=2)
        self.entry_email.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="Carrera:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=12, column=0, padx=20,
                                                                                           pady=1, sticky="w")
        self.entry_carrera = Entry(self, bg="#183c54", width=30)
        self.entry_carrera.grid(row=13, column=0, padx=20, pady=2)
        self.entry_carrera.config(fg="#F0F8FF", justify="center", font="arial, 9")

        Label(self, text="Ingreso (YYYY):", justify="left", bg=fondo, fg=texto, font=campos).grid(row=14, column=0,
                                                                                                  padx=20, pady=1,
                                                                                                  sticky="w")
        self.entry_ingreso = Entry(self, bg="#183c54", width=30)
        self.entry_ingreso.grid(row=15, column=0, padx=20, pady=2)
        self.entry_ingreso.config(fg="#F0F8FF", justify="center", font="arial, 9")

        self.btn_guardar = Button(self, text="Registrar", bg="#28a745", fg=colorBotones, font=botones,
                                  command=self.guardar_estudiante)
        self.btn_guardar.grid(row=16, column=0, padx=20, pady=20)
