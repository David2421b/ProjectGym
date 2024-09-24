#Todo el codigo va aca
import ollama
from dataclasses import dataclass
from datetime import datetime

class Usuario:
    
    def __init__(self, nombre: str, edad: int, email: str, contraseña: str, genero: str, id_persona: str = None):
        self.id_persona: str = id_persona
        self.nombre: str = nombre
        self.edad: int = edad
        self.email: str = email
        self.contraseña: str = contraseña
        self.genero: str = genero


class Rutinas:

    def __init__(self, list_ejercicios: list, nombre_rutina: str, frecuencia_semana: int):
        self.list_ejercicios: list = list_ejercicios
        self.nombre_rutina: str = nombre_rutina
        self.frecuencia_semana: int = frecuencia_semana


class Ejercicio:
    
    def __init__(self, tipo: str, repeticiones: int, series: int, descanso: int, id_ejercicio: str):
        self.tipo: str = tipo
        self.repeticiones_por_serie: int = repeticiones
        self.series: int = series
        self.descanso_entre_series: int = descanso
        self.id_ejercicio: str = id_ejercicio
    
    def modificar_ejercicio(self, repeticiones: int, series: int, descanso: int, duracion: int):
        pass

    def eliminar_ejericio(self, nombre: str, id_ejercicio: str):
        pass
   

class Notificacion:

    def __init__(self, tipo: str, mensaje: str, fecha_hora: datetime):
        self.tipo: str = tipo
        self.mensaje: str = mensaje
        self.fecha_hora: datetime = fecha_hora


class Estadistica:
    imc: int = 0
    tmb: int = 0    
    fcm: int = 0
    
    def calcular_imc(peso: float, altura: float):

        if altura >= 0:
            imc = peso / (altura ** 2)

            if imc < 18.5:
                bienestar = "Te encuentras en Infrapeso"
            
            elif 18.5 <= imc <= 24.9:
                bienestar = "Tu peso es Normal, ¡Sigue asi!"
            
            elif 25 <= imc <= 34.9:
                bienestar = "Tienes Obesidad I, ¡Cuidado!"
            
            elif 35 <= imc <= 39.9:
                bienestar = "Tienes Obesidad II, ¡Cuidado!"

            elif imc >= 40:
                bienestar = "Tienes Obesidad III, ¡Cuidado, deberias visitar a tu medico de confianza!"

        return f"Tu IMC es: {imc} y {bienestar}"

    def calcular_tmb(genero: str, edad: int, peso: float, altura: float):
        if genero == 'Masculino' or genero == 'masculino' or genero == 'M' or genero == 'm':
            tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)
        
        elif genero == 'Femenino' or genero == 'femenino' or genero == 'F' or genero == 'f':
            tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * edad)
        
        else:
            raise ValueError("El genero debe ser hombre o mujer")
        
        return f"Tu TMB es: {tmb}"
        
    def calcular_fcm(edad: int):
        fcm = 220 - edad     
        return f"Tu FCM es: {fcm}"
    

@dataclass
class Chat_Ollama:
    
    def chat(mensaje: str):
        
        if mensaje == 'salir':
            response = "has salido del chat, hasta la proxima"
            return response
        else:
            response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)               
            return response['response']
    
