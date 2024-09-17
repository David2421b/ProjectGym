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
        
    #def modificar_atributo(self, atributo: str, nuevo_valor):
        #Permite modificar un atributo especifico del ejercicio"
        #if atributo == 'tipo':
            #self.tipo = nuevo_valor
        #elif atributo == 'repeticiones':
            #self.repeticiones_por_serie = nuevo_valor
        #elif atributo == 'series':
            #self.series = nuevo_valor
        #elif atributo == 'descanso':
            #self.descanso_entre_series = nuevo_valor
        #elif atributo == 'id_ejercicio':
            #self.id_ejercicio = nuevo_valor
        #else:
            #print(f"Atributo no válido: {atributo}. Los atributos válidos son: tipo, repeticiones, series, descanso, id_ejercicio.")

#ejercicio = Ejercicio(tipo='Sentadillas', repeticiones_por_serie=12, series=4, descanso_entre_series=60, id_ejercicio='EJ001')


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
        fcm = 220 - Usuario.edad   #Consulta sobre uso de self
        return fcm

    def calcular_calorias_quemadas(self, duracion: float, intensidad: float):
        pass

    def medir_vo2_max(self):
        pass    # no se como calcularlo

    def calcular_presion_arterial_promedio(self, presiones: list[tuple[float, float]]):
        pass                # invesitgar acerca del uso de la tupla

    def calcular_glucosa_promedio(self, niveles: list[float]):
        self.niveles: list[float] = niveles     # no se como calcularlo
    
    def evaluar_bienestar_general(): #Metodo en proceso
        pass

    def __str__(self) -> str:       # Revisar si es mejor un dunder para cada metodo o uno general
        return f"""Tu IMC es {self.IMC} y {self.bienestar} \n
                   Tu TMB es {self.tmb} \n
                   Tu FCM es {self.fcm} \n
                   Tus calorias quemadas son {self.calorias_quemadas} \n
                   Tu VO2 maximo es {self.vo2_max} \n
                   Tu presion arterial promedio es {self.presion_arterial_promedio} \n
                   Tu glucosa promedio es {self.glucosa_promedio} \n
                   Tu bienestar general es {self.bienestar_general} \n"""

class Ollama:

    def chat(mensaje):
        if mensaje == 'salir':
            response = "has salido del chat, hasta la proxima"
            return response
        else:
            response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)               
            return response['response']
    


# pruebas del chat con ollama
persona1 = Usuario('Juan', '123', 20, 'davidmejia0951@gmail.com', 'Masculino', '2002-09-05')
print(persona1.nombre)

Mensaje = input("\n Si desea salir del chat solo escriba 'Salir' \n Cual es tu pregunta: ")

print(Ollama.chat(Mensaje))



# fin de pruebas del chat con ollama

# Consultar la posibilidad de que el ususario elija el sexo mediante un numero y que el programa lo convierta en el nombre correspondiente
