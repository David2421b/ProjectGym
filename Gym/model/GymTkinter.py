import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Etiqueta")
label.grid(row=0, column=0)

entry = tk.Entry(root)
entry.grid(row=0, column=1)

button = tk.Button(root, text="Botón")
button.grid(row=1, column=0, columnspan=2, sticky="we")

root.mainloop()
