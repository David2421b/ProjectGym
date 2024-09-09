#Todo el codigo va aca
import ollama

class Usuario:
    
     def __init__(self, nombre: str, edad: int, genero: str, peso: float, altura: float):
        self.nombre: str = nombre
        self.edad: int = edad
        self.genero: str = genero
        self.peso: float = peso
        self.altura: float = altura
    





class Ejercicios:
    
    def __init__(self, tipo: str, repeticiones: int, series: int, descanzo: int):
        self.tipo: str = tipo
        self.repeticiones: int = repeticiones
        self.series: int = series
        self.descanzo: int = descanzo




















# aca inicio el uso de Ollama
def chatOllama(mensaje):
    if mensaje == 'salir':
        response = "has salido del chat, hasta la proxima"
        return response
    else:
        response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)
        return response['response']

Mensaje = input("Si desea salir del chat solo escriba 'Salir' \n Cual es tu pregunta: ")

print(chatOllama(Mensaje))

# FInaliza el uso de Ollamaa