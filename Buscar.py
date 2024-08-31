from tkinter import *
from Listado import Listado

class Buscar(Frame):
    
    def __init__(self, master = None):
        super().__init__(master,width=None)
        self.master = master
        self.pack()
        self.configure(bg="#183c54")
        self.crear_widgets()

    def crear_widgets(self):
        
        self.campos = ("Arial", 10)
        self.titulo = ("Arial", 16, "bold")
        self.botones=("Tahoma", 9)
        self.colorBotones =  "#183c54"

        self.titulo = Label(self, text="BIENVENIDOS A \n GESTION DE ESTUDIANTES", justify='center', fg="#FFFFFF",bg="#183c54", font=self.titulo)
        self.titulo.grid(row=0, column=0, columnspan=4, pady=50)
         
        self.Legajo = Label(self, text="Legajo:", anchor="w", justify="left", bg="#183c54", fg="#FFFFFF", font=self.campos)
        self.Legajo.grid(row=1, column=0, padx=15, sticky="w")
        # creacion borde y color.
        self.borde_color = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color.grid(row=2, column=0, columnspan=4, padx=15, pady=8, sticky="ew") # posicionamiento
        # Cuadro de texto dentro del Frame con borde
        self.cuadro_Legajo = Entry(self.borde_color,bg="#183c54")
        self.cuadro_Legajo.pack(fill="both", expand=True)  # Rellenar el espacio del Frame
        self.cuadro_Legajo.config(fg="#F0F8FF",justify="center",font="arial, 9")  # color de texto
       
        self.Dni = Label(self, text="Dni:", anchor="w", justify="left", bg="#183c54", fg="#FFFFFF", font=self.campos)
        self.Dni.grid(row=3, column=0, padx=15, sticky="w")
        # creacion borde y color.
        self.borde_color2 = Frame(self, bg="#FFFFFF", padx=1, pady=1)  
        self.borde_color2.grid(row=4, column=0, columnspan=4, padx=15, pady=8, sticky="ew") # posicionamiento
        # Cuadro de texto dentro del Frame con borde
        self.cuadro_Dni = Entry(self.borde_color2,bg="#183c54")
        self.cuadro_Dni.pack(fill="both", expand=True)
        self.cuadro_Dni.config(fg="#F0F8FF",justify="center",font="arial, 9")

        self.BotonAgregar = Button(self, text="Agregar",bg="#FFFFFF",font=self.botones,fg=self.colorBotones, command=self.abrir_agregar ).grid(row=5, column=0, padx=30, pady=40,sticky="ew" )
        self.BotonBuscar= Button(self, text="Buscar",bg="#FFFFFF",font=self.botones,fg=self.colorBotones).grid(row=5, column=3, padx=30, pady=40, sticky="ew")


    def abrir_agregar(self):
        # Crea una nueva ventana para el menú
        ventana_agregar = Toplevel(self.master)
        ventana_agregar.geometry("550x300")
        ventana_agregar.resizable
        Listado(ventana_agregar)




'''
root = Tk()
root.geometry("360x400")
root.configure(bg="#183c54")
app = Buscar(master=root)
app.mainloop()
'''