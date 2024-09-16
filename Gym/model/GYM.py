#Todo el codigo va aca
import ollama
from dataclasses import dataclass
from datetime import datetime



class Usuario:
    
     def __init__(self, nombre: str, id_persona: str, edad: int, email: str, genero: str, fecha_nacimiento: str):
        self.nombre: str = nombre
        self.id_persona: str = id_persona
        self.edad: int = edad
        self.email: str = email
        self.genero: str = genero
        self.fecha_nacimiento: str = fecha_nacimiento

    
     def guardar_informacion(self):
        pass
     
     def cargar_informacion(self):
        pass
    


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


class Historial_medico:

    def __init__(self, fecha: datetime, peso: float, altura: float, presion_arterial: float, frecuencia_cardiaca: float):
        self.fecha: datetime = fecha
        self.peso:float = peso
        self.altura: float = altura
        self.presion_arterial: float = presion_arterial
        self.frecuencia_cardiaca: float = frecuencia_cardiaca


class Notificacion:

    def __init__(self, tipo: str, mensaje: str, fecha_hora: datetime):
        self.tipo: str = tipo
        self.mensaje: str = mensaje
        self.fecha_hora: datetime = fecha_hora

@dataclass
class Estadistica:

    def obtener_datos_medicos(self, historial_medico):
        pass
    
    def calcular_imc(self):
        self.IMC = Historial_medico.peso / (Historial_medico.altura ** 2)
    
    def __str__(self) -> str:
        return f"Tu IMC es {self.IMC}"
        
        

@dataclass
class Ollama:

    def chat(mensaje):
        if mensaje == 'salir':
            response = "has salido del chat, hasta la proxima"
            return response
        else:
            response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)               
            return response['response']


Mensaje = input("\n Si desea salir del chat solo escriba 'Salir' \n Cual es tu pregunta: ")

print(Ollama.chat(Mensaje))
