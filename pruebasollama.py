import sys
import os

from nicegui import *
from dataclasses import dataclass


from GYM.model.DigitalHealth import *
from GYM.Logic.DataBase import Database



    
mensaje = ui.input("Cual es tu pregunta: ").style("margin-bottom: 10px; width: 100%;")
ui.button("Enviar", on_click = lambda: enviar(mensaje.value)).style("margin-bottom: 10px; width: 100%;")
    
def enviar(mensaje):
    respuesta = Chat_Ollama.chat(mensaje)
    ui.label(respuesta)


ui.run()