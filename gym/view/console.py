import time
import sys
import os
sys.path.append("GYM")
from model.DigitalHealth import Usuario, Chat_Ollama, Estadistica
from Logic.DataBase import Database


def menu(db):

    print("\n Bienvenido a la aplicación de DigitalHealth!")
    time.sleep(0.8)

    while True:
        print("\n-------------- MENÚ -------------- \n")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir \n")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario(db)
        elif opcion == "2":
            iniciar_sesion(db)
        elif opcion == "3":
            print("Saliendo del programa...")
            db.close()
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def registrar_usuario(db):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    email = input("Email: ")
    contraseña = input("Contraseña: ")
    genero = input("Género: ")
    
    usuario = Usuario(nombre, edad, email, contraseña, genero)
    db.registrar_usuario(usuario)



def iniciar_sesion(db):
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    exito, usuario = db.verificar_credenciales(email, contraseña)

    if exito:
        print(f"Bienvenido/a, {usuario[1]}!")
        consul_Chat = input("""Bienvenido a la aplicacion de DigitalHealth \n
                                si deseas chatear con un META IA escribe "1"
                                si deseas conocer tu IMC, TMB y FCM escribe "2": """)

        if consul_Chat == '1':
            print("Chat iniciado")
            time.sleep(0.8)
            mensaje = input("Cual es tu pregunta: ")
            while mensaje != "salir" or "Salir":
                print(Chat_Ollama.chat(mensaje))
                mensaje = input("Cual es tu pregunta: ")
        
        elif consul_Chat == '2':
            peso = float(input("Ingresa tu peso en Kg: "))
            altura = float(input("Ingresa tu altura en Mts: "))
            genero = usuario[5]
            edad = usuario[2]
            
            print("Calculando...\n")
            time.sleep(1)
            print(f"{Estadistica.calcular_imc(peso, altura)} \n")
            print(f"{Estadistica.calcular_tmb(genero, edad, peso, altura)} \n")
            print(f"{Estadistica.calcular_fcm(edad)} \n")
    else:
        print("Error: credenciales incorrectas.")

if __name__ == "__main__":
    # Inicializamos la base de datos
    db = Database()
    db.connect()
    menu(db)