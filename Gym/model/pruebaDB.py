import mysql.connector

# Clase Usuarios
class Usuarios:
    def __init__(self, nombre, edad, email, contraseña, genero):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.contraseña = contraseña
        self.genero = genero

    # Método para mostrar los datos del usuario
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.email}, Género: {self.genero}")

# Función para insertar un usuario en la base de datos
def insertar_usuario_en_bd(usuario):
    try:
        # Conectar a la base de datos
        conexion = mysql.connector.connect(
            host="localhost",      # Cambiar si tu servidor MySQL está en otro host
            user="root",     # Cambia 'tu_usuario' por tu usuario de MySQL
            password="", # Cambia 'tu_contraseña' por tu contraseña de MySQL
            database="digital_health"  # Base de datos a la que se conectará
        )

        cursor = conexion.cursor()

        # Consulta SQL para insertar un nuevo usuario
        sql = """
        INSERT INTO usuarios (nombre, edad, email, contraseña, genero)
        VALUES (%s, %s, %s, %s, %s)
        """
        valores = (usuario.nombre, usuario.edad, usuario.email, usuario.contraseña, usuario.genero)

        cursor.execute(sql, valores)
        conexion.commit()

        print("Usuario insertado correctamente en la base de datos.")

    except mysql.connector.Error as error:
        print(f"Error al insertar en la base de datos: {error}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()

# Función para solicitar datos al usuario
def solicitar_datos_usuario():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    email = input("Ingrese su email: ")
    contraseña = input("Ingrese su contraseña: ")
    genero = input("Ingrese su género: ")
    
    # Crear una instancia de la clase Usuarios
    nuevo_usuario = Usuarios(nombre, edad, email, contraseña, genero)
    
    # Insertar el usuario en la base de datos
    insertar_usuario_en_bd(nuevo_usuario)

# Llamar a la función para solicitar los datos e insertarlos
solicitar_datos_usuario()
