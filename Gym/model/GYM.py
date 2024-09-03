#Todo el codigo va aca
import ollama
import tkinter as tk

# aca inicio el uso de Ollama
def chatOllama(mensaje):
    if mensaje == 'salir':
        response = "has salido del chat, hasta la proxima"
        return response
    else:
        response = ollama.generate(model = 'llama3.1:latest', prompt = mensaje)
        return response['response']

Mensaje = input(" Bienvenido al chat de META!!! \n Si desea salir del chat solo escriba 'Salir'\n Cual es tu pregunta: ")

print(chatOllama(Mensaje))

# FInaliza el uso de Ollama