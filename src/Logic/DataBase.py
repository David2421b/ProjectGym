import sqlite3
import os
from DigitalHealth import Usuario

class Database:
    def __init__(self, db_name='digitalhealth.db'):
        # Aseguramos que la base de datos se crea en la carpeta especificada
        self.db_name = os.path.join(os.path.dirname(__file__), 'database', db_name)
        self.conexion = None

    def connect(self):
        try:
            # Conectar a la base de datos SQLite
            self.conexion = sqlite3.connect(self.db_name)
            print(f"Conexión exitosa a la base de datos en: {self.db_name}")
            self.crear_tabla_usuarios()
        except sqlite3.Error as err:
            print(f"Error de conexión: {err}")
            self.conexion = None

    def crear_tabla_usuarios(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    contraseña TEXT NOT NULL,
                    genero TEXT NOT NULL
                )
            ''')
            self.conexion.commit()
            cursor.close()
            print("Tabla 'usuarios' creada correctamente o ya existía.")
        else:
            print("No se pudo crear la tabla. No hay conexión con la base de datos.")

    def registrar_usuario(self, usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO usuarios (nombre, edad, email, contraseña, genero)
                    VALUES (?, ?, ?, ?, ?)
                ''', (usuario.nombre, usuario.edad, usuario.email, usuario.contraseña, usuario.genero))
                self.conexion.commit()
                print("Usuario registrado correctamente.")
            except sqlite3.Error as error:
                print(f"Error al registrar usuario: {error}")
            finally:
                cursor.close()

    def verificar_credenciales(self, email, contraseña):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE email = ? AND contraseña = ?', (email, contraseña))
            usuario = cursor.fetchone()
            cursor.close()

            if usuario:
                return True, usuario  # Devuelve True y el registro del usuario
            else:
                return False, None  # Si no se encuentra coincidencia
        return False, None

    def close(self):
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
