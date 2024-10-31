import ollama
from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar

class Usuario:
    
    def __init__(self, nombre: str, edad: int, email: str, contraseña: str, genero: str, id_persona: str = None):
        self.nombre: str = nombre
        self.edad: int = edad
        self.email: str = email
        self.contraseña: str = contraseña
        self.genero: str = genero
        self.id_persona: str = id_persona


class Rutinas:

    def __init__(self, list_ejercicios: list, nombre_rutina: str, frecuencia_semana: int):
        self.list_ejercicios: list = list_ejercicios
        self.nombre_rutina: str = nombre_rutina
        self.frecuencia_semana: int = frecuencia_semana


class Ejercicio:
    
    def __init__(self, nombre: str, tipo: str, repeticiones: int, series: int, descanso: int, id_persona: str):
        self.id_ejercicio: str = None
        self.nombre: str = nombre
        self.tipo: str = tipo
        self.repeticiones_por_serie: int = repeticiones
        self.series: int = series
        self.descanso_entre_series: int = descanso
        self.id_persona: str = id_persona
    
    def modificar_ejercicio(self, repeticiones: int, series: int, descanso: int, duracion: int):
        pass

    def eliminar_ejericio(self, nombre: str, id_ejercicio: str):
        pass
   

class Notificacion:

    def __init__(self, tipo: str, mensaje: str, fecha_hora: datetime):
        self.tipo: str = tipo
        self.mensaje: str = mensaje
        self.fecha_hora: datetime = fecha_hora

    def __str__(self) -> str:
        return f'{self.tipo}: {self.mensaje} - {self.fecha_hora}'

@dataclass
class Estadistica:

    imc: ClassVar[int] = 0
    tmb: ClassVar[int] = 0    
    fcm: ClassVar[int] = 0
    
    def calcular_imc(peso: float, altura: float):
        if altura >= 0:
            imc = peso / (altura ** 2)
        return imc

    def calcular_tmb(genero: str, edad: int, peso: float, altura: float):
        if genero == "Hombre":
            tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
        
        elif genero == "Mujer":
            tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
        return tmb
        
    def calcular_fcm(edad: int):
        fcm = 220 - edad     
        return fcm
    

@dataclass
class Chat_Ollama:
    
    def chat(mensaje: str):
        response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje) #generate devuelve un diccionario y el metodo extrae el valor asociado a response
        return response['response']  #retorna la respuesta