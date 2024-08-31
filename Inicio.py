from tkinter import *
from Buscar import Buscar


ventana = Tk()
ventana.title('MiniProyecto')
ventana.geometry("360x400")


# Evitar redimensionar
ventana.resizable(0, 0)

# Logo, color de fondo
ventana.iconbitmap("logo.ico")
ventana.configure(bg="#183c54")

# Crear y agregar el frame del Menu
frame1 = Buscar(ventana)


ventana.mainloop()
