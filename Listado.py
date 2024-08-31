from tkinter import *
'''
root=tk.Tk()
frame_formulario = tk.Frame(root)
frame_formulario.pack(pady=10)



# Añadir los otros campos de la misma manera

btn_guardar = tk.Button(frame_formulario, text="GUARDAR") #command=guardar_alumno#)
btn_guardar.grid(row=3, column=0)

btn_cancelar = tk.Button(frame_formulario, text="CANCELAR") #command=cancelar_operacion#)
btn_cancelar.grid(row=3, column=1)
'''


class Listado (Frame):

    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.configure(bg="#183c54")
        self.crear_listado()  
    
    def crear_listado(self):
        
        campos = ("Arial", 10)
        fondo = "#183c54"
        texto = "#FFFFFF"

        # Crear y ubicar las etiquetas y campos de entrada
        Label(self, text="Legajo:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=0, column=0, padx=20, pady=1, sticky="w")
        self.entry_legajo = Entry(self, bg="#FFFFFF", width=35)
        self.entry_legajo.grid(row=1, column=0, padx=20, pady=10,sticky="ew")

        Label(self, text="DNI:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=0, column=2, padx=20, pady=1, sticky="w")
        self.entry_dni = Entry(self, bg="#FFFFFF",width=35)
        self.entry_dni.grid(row=1, column=2, padx=20, pady=5, sticky="ew")

        Label(self, text="Nombre y Apellido:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=2, column=0, padx=20, pady=1, sticky="w")
        self.entry_nombre_apellido = Entry(self, bg="#FFFFFF")
        self.entry_nombre_apellido.grid(row=3, column=0, padx=20, pady=5, sticky="ew")
        
        Label(self, text="Nacimiento:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=2, column=2, padx=20, pady=1, sticky="w")
        self.entry_nacimiento = Entry(self, bg="#FFFFFF")
        self.entry_nacimiento.grid(row=3, column=2, padx=20, pady=5, sticky="ew")

        Label(self, text="Domicilio:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=4, column=0, padx=20, pady=1, sticky="w")
        self.entry_domicilio = Entry(self, bg="#FFFFFF")
        self.entry_domicilio.grid(row=5, column=0, padx=20, pady=5, sticky="ew")

        Label(self, text="Email:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=4, column=2, padx=20, pady=1, sticky="w")
        self.entry_email = Entry(self, bg="#FFFFFF")
        self.entry_email.grid(row=5, column=2, padx=20, pady=5, sticky="ew")

        Label(self, text="Carrera:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=6, column=0, padx=20, pady=1, sticky="w")
        self.entry_carrera = Entry(self, bg="#FFFFFF")
        self.entry_carrera.grid(row=7, column=0, padx=20, pady=5, sticky="ew")

        Label(self, text="Año de ingreso:", justify="left", bg=fondo, fg=texto, font=campos).grid(row=6, column=2, padx=20, pady=1, sticky="w")
        self.entry_anio_ingreso = Entry(self, bg="#FFFFFF")
        self.entry_anio_ingreso.grid(row=7, column=2, padx=20, pady=5, sticky="ew")
        




root=Tk()
app = Listado(master=root)
#root.geometry("500x500")
#root.configure(bg="#183c54")
app.mainloop()