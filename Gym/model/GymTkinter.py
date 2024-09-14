import tkinter as tk

class Interfaz:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Chat de Meta")
        self.ventana.attributes('-fullscreen', True)
        self.crea_widget()
    
    def crea_widget(self):
        # Etiqueta de bienvenida
        self.bienvenida = tk.Label(self.ventana, text="Bienvenido al chat de Meta!!!", background="gray", font=("Arial", 25))
        self.bienvenida.pack(fill=tk.X)
    
        # Marco para los botones
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack()

        # Botón de salir
        self.boton1 = tk.Button(self.frame_botones, text="Salir", padx=30, pady=5, command=self.ventana.quit)
        self.boton1.pack(side=tk.LEFT)

        # Botón para activar el chat
        self.btn_ollama = tk.Button(self.frame_botones, text="Ollama", padx=30, pady=5, command=self.activar_chat)
        self.btn_ollama.pack(side=tk.LEFT)

        # Entrada de texto
        self.entrada = tk.Entry(self.ventana, width=50)
        self.entrada.pack()

    def activar_chat(self):
        texto = self.entrada.get()
        print(f"Texto de entrada: {texto}")

def main():
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()
