import sqlite3
import os
  

class Database:
    def __init__(self, db_name='digitalhealth.db'):
        # Aseguramos que la base de datos se crea en la carpeta especificada
        self.db_name = os.path.join(os.path.dirname(__file__), 'database', db_name)
        self.conexion = None

    def connect(self):
        try:
            # Conectar a la base de datos SQLite
            self.conexion = sqlite3.connect(self.db_name, check_same_thread = False)
            self.crear_tabla_usuarios()
            self.crear_tabla_ejercicios()

        except sqlite3.Error as err:
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

    def crear_tabla_ejercicios(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ejercicios (
                    id_ejercicio INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_persona INTEGER NOT NULL,
                    nombre TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    repeticiones INTEGER NOT NULL,
                    series INTEGER NOT NULL,
                    descanso_series INTEGER NOT NULL,

                    FOREIGN KEY (id_persona) REFERENCES usuarios(id_persona)
                )
            ''')
            self.conexion.commit()
            cursor.close()

    def registrar_usuario(self, usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO usuarios (nombre, edad, email, contraseña, genero)
                    VALUES (?, ?, ?, ?, ?)
                ''', (usuario.nombre, usuario.edad, usuario.email, usuario.contraseña, usuario.genero))
                self.conexion.commit()

            except sqlite3.Error as error:
                error
                
            finally:
                cursor.close()
    
    def registrar_ejercicio(self, ejercicio):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO ejercicios (id_persona, nombre, tipo, repeticiones, series, descanso_series)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (ejercicio.id_persona, ejercicio.nombre, ejercicio.tipo, ejercicio.repeticiones, ejercicio.series, ejercicio.descanso_entre_series))
                self.conexion.commit()

            except sqlite3.Error as error:
                error
                
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
