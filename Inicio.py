from tkinter import *
from Buscar import Buscar

#Configuracion ventana
ventana = Tk()
ventana.title('MiniProyecto')
ventana.geometry("360x400")
ventana.resizable(0, 0)  #Evitar redimensionar
ventana.iconbitmap("logo.ico") 
ventana.configure(bg="#183c54")


# Crear y agregar el frame al inicio
frame1 = Buscar(ventana)






ventana.mainloop()
