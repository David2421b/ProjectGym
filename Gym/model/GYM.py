#Todo el codigo va aca
import ollama

class Usuario:
    
     def __init__(self, nombre: str, edad: int, genero: str, peso: float, altura: float, PresArterial: int, frecardiac):
        self.nombre: str = nombre
        self.edad: int = edad
        self.genero: str = genero
        self.peso: float = peso
        self.altura: float = altura
        
        self.historial_medico = {
            'peso': [peso],
            'presion_arterial': [],
            'frecuencia_cardiaca': [],
            'glucosa_en_sangre': []
        }
        
        self.preferencias = {
            'recordatorios': True,
            'mensajes': True
        }
        
        #analizar si es necesario este metodo dentro de esta clase o si mejor lo dejamos como clase
        def actualizar_historial_medico(self, peso = None, presion_arterial = None, frecuencia_cardiaca = None, glucosa = None):
        if peso:  #Corregir el condicional If para que la linea funcione
            self.peso = peso
            self.historial_medico['peso'] = peso
        if presion_arterial:
            self.historial_medico['presion_arterial'].append(presion_arterial)  #incongruencia en la linea 27 con respecto a la variable presion_arterial
        if frecuencia_cardiaca:
            self.historial_medico['frecuencia_cardiaca'].append(frecuencia_cardiaca)
        if glucosa:
            self.historial_medico['glucosa_en_sangre'].append(glucosa)
    


class Ejercicios:
    
    def __init__(self, tipo: str, repeticiones: int, series: int, descanzo: int):
        self.tipo: str = tipo
        self.repeticiones_por_serie: int = repeticiones
        self.series: int = series
        self.descanzo_entre_series: int = descanzo



class Rutinas:

    def __init__(self, list_ejercicios: list, nombre_rutina: str, frecuencia_semana: int, tiempo_estimado = None, estado_progreso = None):
        self.list_ejercicios: list = list_ejercicios
        self.nombre_rutina: str = nombre_rutina
        self.frecuencia_semana: int = frecuencia_semana
        self.tiempo_estimado = tiempo_estimado
        self.estado_progreso = estado_progreso



class Historial_clinico:

    def __init__(self, ):
        pass


class Recordatorios:

    def __init__(self, ):
        pass
        
        
    








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