import tkinter as tk


class Interfaz:

    def __init__(self, ventana):
        self.ventana = ventana

class Interfaz_1(Interfaz):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.ventana.title("Chat de Meta")
        self.ventana.attributes('-fullscreen', True)
        self.crea_widget_1()

    def crea_widget_1(self):
        self.bienvenida = tk.Label(self.ventana, text = "Bienvenido al chat de Meta!!!", background = "gray", font = ("Arial", 25))
        self.bienvenida.pack(fill=tk.X)

        # frame para los botones
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack()

        # salir de la aplicacion
        self.btn_salir = tk.Button(self.frame_botones, text = "Salir", padx = 30, pady = 5, command = self.ventana.destroy)
        self.btn_salir.pack(side = tk.LEFT)

        # entrada de texto
        self.entrada = tk.Entry(self.ventana, width = 50)
        self.entrada.pack()

        # boton para actvar el chat
        self.btn_ollama = tk.Button(self.frame_botones, text = "Ollama", padx = 30, pady = 5, command = self.activar_chat)
        self.btn_ollama.pack(side = tk.RIGHT)

        # boton para cambiar de interfaz
        self.btn_interfaz2 = tk.Button(text = "Interfaz 2", padx = 30, pady = 5, command = self.segunda_ventana)
        self.btn_interfaz2.pack()

    def activar_chat(self):
        self.mensaje = self.entrada.get()
        print(Ollama.chat(self.mensaje))

    def segunda_ventana(self):
        self.ventana.destroy()
        main_2()


class Interfaz_2(Interfaz):

    def __init__(self, ventana):
        super().__init__(ventana)
        self.ventana.title("Segunda Interfaz")
        self.ventana.attributes('-fullscreen', True)
        self.crear_widgets_2()

    def crear_widgets_2(self):
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack()

        self.btn_salir = tk.Button(self.frame_botones, text = "Salir", padx = 30, pady = 5, command = self.ventana.destroy)
        self.btn_salir.pack()

        self.btn_interfaz1 = tk.Button(self.frame_botones, text = "Volver al Inicio", padx = 35, pady = 10, command = self.primera_ventana)
        self.btn_interfaz1.pack()

    def primera_ventana(self):
        self.ventana.destroy()
        main_1()

def main_1():           #Esta funcion inicia la ventana principal
    ventana_1 = tk.Tk()
    app_1 = Interfaz_1(ventana_1)
    ventana_1.mainloop()


def main_2():           #Esta funcion inicia la ventana secundaria
    ventana_2 = tk.Tk()
    app_2 = Interfaz_2(ventana_2)
    ventana_2.mainloop()


main_1()
