from tkinter import *

class Listado (Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=True)
        self.configure(bg="#183c54")
        self.crear_listado()  
    
    def crear_listado(self):
        
        campos = ("Arial", 10)
        fondo = "#183c54"
        texto = "#FFFFFF"
        botones= ("Tahoma", 9)
        colorBotones =  "#183c54"
        

        # Crear y ubicar las etiquetas y campos de entrada
        Label(self, text="Legajo:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        self.borde_color = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color.grid(row=1, column=0, padx=20, pady=2)
        self.entry_legajo = Entry(self.borde_color, bg="#183c54",width=30)
        self.entry_legajo.pack(fill="both", expand=True)
        self.entry_legajo.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="DNI:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=0, column=1, padx=20, pady=1, sticky="w")
        self.borde_color2 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color2.grid(row=1, column=1, padx=20, pady=2)
        self.entry_dni = Entry(self.borde_color2, bg="#183c54",width=30)
        self.entry_dni.pack(fill="both", expand=True)
        self.entry_dni.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="Nombre y Apellido:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        self.borde_color3 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color3.grid(row=3, column=0, padx=20, pady=2)
        self.entry_nombre_apellido = Entry(self.borde_color3, bg="#183c54",width=30)
        self.entry_nombre_apellido.pack(fill="both", expand=True)
        self.entry_nombre_apellido.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="Nacimiento:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=2, column=1, padx=20, pady=1, sticky="w")
        self.borde_color4 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color4.grid(row=3, column=1, padx=20, pady=2)
        self.entry_nacimiento = Entry(self.borde_color4, bg="#183c54",width=30)
        self.entry_nacimiento.pack(fill="both", expand=True)
        self.entry_nacimiento.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="Domicilio:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=4, column=0, padx=20, pady=1, sticky="w")
        self.borde_color5 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color5.grid(row=5, column=0, padx=20, pady=2)
        self.entry_domicilio = Entry(self.borde_color5, bg="#183c54",width=30)
        self.entry_domicilio.pack(fill="both", expand=True)
        self.entry_domicilio.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="Email:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=4, column=1, padx=20, pady=1, sticky="w")
        self.borde_color6 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color6.grid(row=5, column=1, padx=20, pady=2)
        self.entry_email = Entry(self.borde_color6, bg="#183c54",width=30)
        self.entry_email.pack(fill="both", expand=True)
        self.entry_email.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="Carrera:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=6, column=0, padx=20, pady=1, sticky="w")
        self.borde_color7 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color7.grid(row=7, column=0, padx=20, pady=2)
        self.entry_carrera = Entry(self.borde_color7, bg="#183c54",width=30)
        self.entry_carrera.pack(fill="both", expand=True)
        self.entry_carrera.config(fg="#F0F8FF",justify="center",font="arial, 9")

        Label(self, text="Año de ingreso:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=6, column=1, padx=20, pady=1, sticky="w")
        self.borde_color8 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color8.grid(row=7, column=1, padx=20, pady=2)
        self.entry_anio_ingreso = Entry(self.borde_color8, bg="#183c54",width=30)
        self.entry_anio_ingreso.pack(fill="both", expand=True)
        self.entry_anio_ingreso.config(fg="#F0F8FF",justify="center",font="arial, 9")

        self.BotonAgregar = Button(self, text="Guardar",bg="#FFFFFF",font=botones,fg=colorBotones, width=10).grid(row=8, column=0, padx=20, pady=20)
        self.BotonCancelar= Button(self, text="Cancelar",bg="#FFFFFF",font=botones,fg=colorBotones, width=10, command=self.master.destroy).grid(row=8, column=1, padx=20, pady=20)

        


'''
root=Tk()
app = Listado(master=root)
#root.geometry("500x500")
#root.configure(bg="#183c54")
app.mainloop()
'''