from GYM.model.DigitalHealth import Usuario, Chat_Ollama, Estadistica
import time

print("Chat iniciado \n")
time.sleep(0.8)
print("Hola, soy Ollama, tu asistente de salud personal, cuando desees salir solo escribe 'salir' \n")
time.sleep(0.4)
mensaje = input("Cual es tu pregunta: ")
while mensaje != "salir" or "Salir":
    print(Chat_Ollama.chat(mensaje))
    mensaje = input("Cual es tu pregunta: ")