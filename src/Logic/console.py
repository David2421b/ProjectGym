from DigitalHealth import Usuario  # Importamos la clase Usuario
from DataBase import Database  # Importamos la clase Database

def registrar_usuario(db: Database):
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    genero = input("Ingrese su género: ")
    
    usuario = Usuario(nombre, edad, email, contraseña, genero)
    db.registrar_usuario(usuario)

def iniciar_sesion(db: Database):
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    db.verificar_credenciales(email, contraseña)

def menu(db: Database):
    while True:
        print("\nMenú:")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario(db)
        elif opcion == "2":
            iniciar_sesion(db)
        elif opcion == "3":
            print("Saliendo...")
            db.close()
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def ollama():
    Mensaje = input("\n Si desea salir del chat solo escriba 'Salir' \n Cual es tu pregunta: ")
    print(Ollama.chat(Mensaje))


# Configuración de la base de datos y ejecución del menú
if __name__ == "__main__":
    db = Database()
    db.connect()
    menu(db)