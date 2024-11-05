import ollama
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import ClassVar
import time
import random

class Usuario:
    
    def __init__(self, nombre: str, edad: int, email: str, contraseña: str, genero: str, id_persona: str = None):
        self.nombre: str = nombre
        self.edad: int = edad
        self.email: str = email
        self.contraseña: str = contraseña
        self.genero: str = genero
        self.id_persona: str = id_persona


class Rutinas:

    def __init__(self, nombre_rutina: str, list_ejercicios: list):
        self.nombre_rutina: str = nombre_rutina
        self.list_ejercicios: list = list_ejercicios
    
    def agregar_ejercicio(self, ejercicio):
        self.list_ejercicios.append(ejercicio)
        return self.list_ejercicios


class Ejercicio:
    
    def __init__(self, nombre: str, tipo: str, repeticiones: int, series: int, descanso: int):
        self.nombre: str = nombre
        self.tipo: str = tipo
        self.repeticiones: int = repeticiones
        self.series: int = series
        self.descanso_entre_series: int = descanso

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

            if imc < 18.5:
                return f"Tu IMC es: {imc:.1f} y te encuentras en infrapeso"
            elif imc >= 18.5 and imc < 24.9:
                return f"Tu IMC es: {imc:.1f} y te encuentras en un peso normal"
            elif imc >= 25 and imc < 29.9:
                return f"Tu IMC es: {imc:.1f} y te encuentras en sobrepeso"
            elif imc >= 30 and imc < 34.9:
                return f"Tu IMC es: {imc:.1f} y te encuentras en obesidad grado I"
            elif imc >= 35 and imc < 39.9:
                return f"Tu IMC es: {imc:.1f} y te encuentras en obesidad grado II"
            elif imc >= 40:
                return f"Tu IMC es: {imc:.1f} y te encuentras en obesidad grado III"
        return imc

    def calcular_tmb(genero: str, edad: int, peso: float, altura: float):
        if genero == "Hombre":
            tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
        
        elif genero == "Mujer":
            tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
        return f"Tu TMB es: {tmb:.1f}"
        
    def calcular_fcm(edad: int):
        fcm = 220 - edad     
        return f"Tu FCM es: {fcm:.1f}"
    

@dataclass
class Chat_Ollama:
    
    def chat(mensaje: str):
        response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje) #generate devuelve un diccionario y el metodo extrae el valor asociado a response
        return response['response']  #retorna la respuesta


class Vicios(Usuario):
    def __init__(self, nombre, correo, nombre_vicio, compromiso, tracking_duration_days, message_interval_hours, support_messages):
        super().__init__(nombre, correo)  # Heredamos atributos de Usuario
        self.nombre_vicio = nombre_vicio  # Nombre del vicio
        self.compromiso = compromiso  # Compromiso del usuario (ej: "No recaer por 30 días")
        self.start_time = datetime.now()  # Hora de inicio del seguimiento
        self.tracking_duration = timedelta(days=tracking_duration_days)  # Duración del seguimiento
        self.message_interval = timedelta(hours=message_interval_hours)  # Intervalo entre mensajes de apoyo
        self.support_messages = support_messages  # Lista de mensajes de apoyo
        self.relapse_count = 0  # Contador de recaídas
        self.last_relapse_date = None  # Fecha de última recaída
        self.ultimo_mensaje = datetime.now()  # Marca de tiempo del último mensaje



class Vicio:
    def __init__(self, id_persona, nombre_vicio, fecha_dejar, compromiso):
        self.id_persona = id_persona
        self.nombre_vicio = nombre_vicio
        self.fecha_dejar = fecha_dejar
        self.compromiso = compromiso

class Sentimiento:
    def __init__(self, id_persona, fecha, sentimiento, descripcion):
        self.id_persona = id_persona
        self.fecha = fecha
        self.sentimiento = sentimiento
        self.descripcion = descripcion
