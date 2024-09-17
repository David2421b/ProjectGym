from database import Database
from DigitalHealth import Usuario

def menu(db):
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
    else:
        print("Error: credenciales incorrectas.")

if __name__ == "__main__":
    # Inicializamos la base de datos
    db = Database()
    db.connect()
    menu(db)