import ollama
from dataclasses import dataclass
from datetime import datetime
import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Conectar a la base de datos"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def disconnect(self):
        """Cerrar la conexión a la base de datos"""
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")

    def insertar_usuario(self, usuario):
        """Insertar los datos del objeto Usuario en la base de datos"""
        cursor = self.connection.cursor()
        query = """INSERT INTO usuarios (nombre, edad, email, contraseña, genero, fecha_nacimiento, id_persona) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        data = (
            usuario.nombre, usuario.edad, usuario.email, usuario.contraseña, 
            usuario.genero, usuario.fecha_nacimiento, usuario.id_persona
        )
        
        try:
            cursor.execute(query, data)
            self.connection.commit()  # Confirmar los cambios
            print("Usuario insertado correctamente")
        except Error as e:
            print(f"Error al insertar usuario: {e}")
        finally:
            cursor.close()        


class Usuario:
    
    def __init__(self, nombre: str, id_persona: str, edad: int, email: str, genero: str, fecha_nacimiento: str):
        self.nombre: str = nombre
        self.id_persona: str = id_persona
        self.edad: int = edad
        self.email: str = email
        self.genero: str = genero
        self.fecha_nacimiento: str = fecha_nacimiento


            
    def guardar_informacion(self):
        pass
     
    def cargar_informacion(self):
        pass

        usuario = Usuario(
    nombre="Juan Pérez", edad=30, email="juan.perez@example.com", 
    contraseña="mi_contraseña_segura", genero="Masculino", 
    fecha_nacimiento="1990-01-01"
)

# Conectar y añadir el usuario a la base de datos
db = Database(host="localhost", user="root", password="", database="")
db.connect()
db.insertar_usuario(usuario)
db.disconnect()  


# Crear una instancia de la clase Usuario
  