import tkinter


ventana = tkinter.Tk()
ventana.geometry("800x700")


Bienvenida = tkinter.Label(ventana, text="Bienvenido al chat de META!!!", background="gray", font=("Arial", 25))
Bienvenida.pack(fill=tkinter.X)

boton1 = tkinter.Button(ventana, text="Salir", padx=30, pady=5)
boton1.pack()
ventana.mainloop()