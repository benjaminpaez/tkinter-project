from tkinter import *
from Buscar import Buscar



ventana = Tk()
ventana.title('MiniProyecto')
ventana.geometry("360x400")
ventana.resizable(0, 0)
ventana.iconbitmap("logo.ico") 
ventana.configure(bg="#183c54")


frame1 = Buscar(ventana)

ventana.mainloop()
