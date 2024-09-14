#Todo el codigo va aca
import ollama
from dataclasses import dataclass
import tkinter as tk

class Interfaz:
    
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Chat de Meta")
        self.ventana.attributes('-fullscreen', True)
        self.crea_widget()
    
    def crea_widget(self):
        self.bienvenida = tk.Label(self.ventana, text = "Bienvenido al chat de Meta!!!", background = "gray", font = ("Arial", 25))
        self.bienvenida.pack(fill=tk.X)

        # frame para los botones
        self.frame_botones = tk.Frame(self.ventana)
        self.frame_botones.pack()
    
        # salir de la aplicacion
        self.btn_salir = tk.Button(self.frame_botones, text = "Salir", padx = 30, pady = 5, command = self.ventana.destroy)        
        self.btn_salir.pack(side = tk.LEFT)

        # entrada de texto
        self.entrada = tk.Entry(self.ventana, width=50)
        self.entrada.pack()

        # boton para actvar el chat
        self.btn_ollama = tk.Button(self.frame_botones, text = "Ollama", padx = 30, pady = 5, command = self.activar_chat)
        self.btn_ollama.pack(side = tk.RIGHT)
    
    def activar_chat(self):
        self.mensaje = self.entrada.get()
        print(Ollama.chat(self.mensaje))
    

def main():
    ventana = tk.Tk()
    app = Interfaz(ventana)
    ventana.mainloop()
    



class Usuario:
    
     def __init__(self, nombre: str, edad: int, email: str, genero: str, fecha_nacimiento: str, id_persona: str):
        self.nombre: str = nombre
        self.edad: int = edad
        self.email: str = email
        self.genero: str = genero
        self.fecha_nacimiento: str = fecha_nacimiento
        self.id_persona: str = id_persona
        

class Rutinas:

    def __init__(self, list_ejercicios: list, nombre_rutina: str, frecuencia_semana: int, tiempo_estimado = None, estado_progreso = None):
        self.list_ejercicios: list = list_ejercicios
        self.nombre_rutina: str = nombre_rutina
        self.frecuencia_semana: int = frecuencia_semana
        self.tiempo_estimado = tiempo_estimado
        self.estado_progreso = estado_progreso


class Ejercicios:
    
    def __init__(self, tipo: str, repeticiones: int, series: int, descanzo: int, id_ejercicio: str):
        self.tipo: str = tipo
        self.repeticiones_por_serie: int = repeticiones
        self.series: int = series
        self.descanzo_entre_series: int = descanzo
        self.id_ejercicio: str = id_ejercicio


class Historial_clinico:

    def __init__(self):
        pass


class Recordatorios:

    def __init__(self):
        pass
        

@dataclass
class Ollama:

    def chat(mensaje):
        if mensaje == 'salir':
            response = "has salido del chat, hasta la proxima"
            return response
        else:
            response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)
            return response['response']

main() #con esta linea empezamos a ejecutar la interfaz

Mensaje = input("Si desea salir del chat solo escriba 'Salir' \n Cual es tu pregunta: ")

print(Ollama.chat(Mensaje))
