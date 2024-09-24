from GYM.model.DigitalHealth import Usuario, Chat_Ollama, Estadistica
import time

print("Chat iniciado")
time.sleep(0.8)
mensaje = input("Cual es tu pregunta: ")        
print(Chat_Ollama.chat(mensaje))