#Todo el codigo va aca

import ollama
from dataclasses import dataclass
from datetime import datetime
import mysql.connector
from mysql.connector import Error


class Usuario:
    
    def __init__(self, nombre: str, edad: int, email: str, contraseña: str, genero: str, fecha_nacimiento: str,  id_persona: str = None):
        self.id_persona: str = id_persona
        self.nombre: str = nombre
        self.edad: int = edad
        self.email: str = email
        self.contraseña: str = contraseña
        self.genero: str = genero
        self.fecha_nacimiento: str = fecha_nacimiento
    
    def arranque_app(self, seleccion):
        self.seleccion = seleccion

    
    def solicitar_datos_usuario(self):
        print("Por favor, ingrese los siguientes datos generales:")
        self.datos_usuario['peso'] = float(input("Peso (kg): "))
        self.datos_usuario['altura'] = float(input("Altura (cm): "))
        self.datos_usuario['temperatura_corporal'] = float(input("Temperatura Corporal (°C): "))
        
    def registrarse(self):
        pass
     
    def iniciar_sesion(self):
        pass

class Rutinas:

    def __init__(self, list_ejercicios: list, nombre_rutina: str, frecuencia_semana: int):
        self.list_ejercicios: list = list_ejercicios
        self.nombre_rutina: str = nombre_rutina
        self.frecuencia_semana: int = frecuencia_semana
       
class Ejercicio:
    
    def __init__(self, tipo: str, repeticiones: int, series: int, descanzo: int, id_ejercicio: str):
        self.tipo: str = tipo
        self.repeticiones_por_serie: int = repeticiones
        self.series: int = series
        self.descanzo_entre_series: int = descanzo
        self.id_ejercicio: str = id_ejercicio
    
    def modificar_ejercicio(self, repeticiones: int, series: int, descanso: int, duracion: int):
        pass

    def eliminar_ejericio(self, nombre: str, id_ejercicio: str):
        pass


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


class Estadistica:
    
    def calcular_imc(self):
        if Historial_medico.altura >= 0:
            self.IMC = Historial_medico.peso / (Historial_medico.altura ** 2)

            if self.IMC < 18.5:
                self.bienestar = "Te encuentras en Infrapeso"
            
            elif 18.5 <= self.IMC <= 24.9:
                self.bienestar = "Tu peso es Normal,¡Sigue asi!"
            
            elif 25 <= self.IMC <= 34.9:
                self.bienestar = "Tienes Obesidad I, ¡Cuidado!"
            
            elif 35 <= self.IMC <= 39.9:
                self.bienestar = "Tienes Obesidad II, ¡Cuidado!"

            elif self.IMC >= 40:
                self.bienestar = "Tienes Obesidad III, ¡Cuidado, visita un medico de confianza!"

    def calcular_tmb(self):
        if Usuario.genero == 'Masculino' or Usuario.genero == 'masculino' or Usuario.genero == 'M' or Usuario.genero == 'm':
            self.tmb = 88.362 + (13.397 * Historial_medico.peso) + (4.799 * Historial_medico.altura) - (5.677 * Usuario.edad)
        
        elif Usuario.genero == 'Femenino' or Usuario.genero == 'femenino' or Usuario.genero == 'F' or Usuario.genero == 'f':
            self.tmb = 447.593 + (9.247 * Historial_medico.peso) + (3.098 * Historial_medico.altura) - (4.330 * Usuario.edad)
        
        else:
            raise ValueError("El genero debe ser hombre o mujer")
        
    def calcular_fcm(self):
        self.fcm = 220 - Usuario.edad     
    
    def evaluar_bienestar_general(): #Metodo en proceso
        pass

    def __str__(self) -> str: 
        return f"""Tu IMC es {self.IMC} y {self.bienestar} \n
                   Tu TMB es {self.tmb} \n
                   Tu FCM es {self.fcm} \n
                   Tu bienestar general es {self.bienestar_general} \n"""

class Ollama:

    def chat(mensaje):
        if mensaje == 'salir':
            response = "has salido del chat, hasta la proxima"
            return response
        else:
            response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)               
            return response['response']
    

#------------------------------------------------------Arranque de la aplicacion---------------------------------------------------------#
# pruebas del chat con ollama
inicio_app = int(input("""\n Bienvenido a nuestro Gym Virtual \n 
                       si deseas iniciar sesión presiona 1 \n 
                       si deseas registrarte presiona 2 \n 
                       si deseas salir presiona 3 \n"""))
                       

if inicio_app == 1:
    Usuario.iniciar_sesion()

elif inicio_app == 2:
    Usuario.registrarse()
            
elif inicio_app == 3:
    print("Hasta la proxima")




Mensaje = input("\n Si desea salir del chat solo escriba 'Salir' \n Cual es tu pregunta: ")
print(Ollama.chat(Mensaje))



# fin de pruebas del chat con ollama

# Consultar la posibilidad de que el ususario elija el sexo mediante un numero y que el programa lo convierta en el nombre correspondiente
