from DataBase import Database
import time
from DigitalHealth import Usuario, Chat_Ollama, Estadistica 


def menu(db):

    print("\n Bienvenido a la aplicación de DigitalHealth!")
    time.sleep(2)

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar nuevo usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
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
            time.sleep(1)
            mensaje = input("Cual es tu pregunta: ")
            print(Chat_Ollama.chat(mensaje))
        
        elif consul_Chat == '2':
            peso = float(input("Ingresa tu peso en Kg: "))
            altura = float(input("Ingresa tu altura en Mts: "))
            
            print("Calculando...\n")
            time.sleep(1)
            print(f"{Estadistica.calcular_imc(peso, altura)} \n")
            print(f"{Estadistica.calcular_tmb(usuario.genero, usuario.edad, peso, altura)} \n")
            print(f"{Estadistica.calcular_fcm(usuario.edad)} \n")
    else:
        print("Error: credenciales incorrectas.")

if __name__ == "__main__":
    # Inicializamos la base de datos
    db = Database()
    db.connect()
    menu(db)