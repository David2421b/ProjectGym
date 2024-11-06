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
            self.crear_tabla_rutinas()
            self.crear_tabla_vicios()         # Nueva tabla vicios
            self.crear_tabla_sentimientos()    # Nueva tabla sentimientos

        except sqlite3.Error as err:
            self.conexion = None

    def crear_tabla_usuarios(self): 

        if self.conexion:  #verificacion de conexion con base de datos
            cursor = self.conexion.cursor() #crea un objeto que permite ejecutar comandos sql
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
            self.conexion.commit() #guarda cambios en la base de datos 
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
    
    def crear_tabla_rutinas(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS rutinas (
                    id_rutina INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_persona INTEGER NOT NULL,
                    nombre_rutina TEXT NOT NULL,
                    Ejercicio1 TEXT,
                    Ejercicio2 TEXT,
                    Ejercicio3 TEXT,
                    Ejercicio4 TEXT,
                    Ejercicio5 TEXT,

                    FOREIGN KEY (id_persona) REFERENCES usuarios(id_persona)
                )
            ''')
            self.conexion.commit()
            cursor.close()

    def registrar_usuario(self, usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:  #manejo de excepciones
                cursor.execute(''' 
                    INSERT INTO usuarios (nombre, edad, email, contraseña, genero)
                    VALUES (?, ?, ?, ?, ?) 
                ''', (usuario.nombre, usuario.edad, usuario.email, usuario.contraseña, usuario.genero))
                self.conexion.commit()  #valores se pasan como tuplas

            except sqlite3.Error as error:
                error
                
            finally:
                cursor.close()
    
    def DNIUsr(Id_Usr: int):
        global Id_usuario #vairable global se puede acceder y modificar desde cualquier 
        Id_usuario = Id_Usr #cualquier valor que se pase a DNIUsr se guardará en Id_usuario
    
    def registrar_ejercicio(self, ejercicio):
        if self.conexion:
            global Id_usuario
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO ejercicios (id_persona, nombre, tipo, repeticiones, series, descanso_series)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (Id_usuario, ejercicio.nombre, ejercicio.tipo, ejercicio.repeticiones, ejercicio.series, ejercicio.descanso_entre_series))
                self.conexion.commit()

            except sqlite3.Error as error:
                error
                
            finally:
                cursor.close()

    def registrar_rutina(self, rutina, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO rutinas (id_persona, nombre_rutina, Ejercicio1, Ejercicio2, Ejercicio3, Ejercicio4, Ejercicio5)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (Id_usuario, rutina.nombre_rutina, rutina.Ejercicio1, rutina.Ejercicio2, rutina.Ejercicio3, rutina.Ejercicio4, rutina.Ejercicio5))
                self.conexion.commit()

            except sqlite3.Error as error:
                error
                
            finally:
                cursor.close()
    
    def obtener_todos_ejercicios(self, Id_usuario):  
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT * FROM ejercicios WHERE id_persona = ?', (Id_usuario,))  #selecciona todos los registros de la tabla ejercicios
            ejercicios = cursor.fetchall()  # Obtiene todos los resultados
            cursor.close()
            return ejercicios
        return []
    
    def obtener_nombres_ejercicios(self, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT nombre FROM ejercicios WHERE id_persona = ?', (Id_usuario,))  # Selecciona solo la columna de nombres
            nombres = cursor.fetchall()  # Obtiene todos los resultados
            cursor.close()
            for i in range(len(nombres)):  #itera sobre cada elemento de la lista nombres 
                nombres[i] = nombres[i][0]  #convierte los nombres en una lista de tuplas
            return nombres
    
    def obtener_tipo_ejercicios(self, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT tipo FROM ejercicios WHERE id_persona = ?', (Id_usuario,))  
            tipo = cursor.fetchall()  # Obtiene todos los resultados
            cursor.close()
            for i in range(len(tipo)):
                tipo[i] = tipo[i][0]
            return tipo
    
    def obtener_repeticiones_ejercicios(self, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT repeticiones FROM ejercicios WHERE id_persona = ?', (Id_usuario,))
            repeticiones = cursor.fetchall()  # Obtiene todos los resultados
            cursor.close()
            for i in range(len(repeticiones)):
                repeticiones[i] = repeticiones[i][0]
            return repeticiones
        
    def obtener_series_ejercicios(self, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT series FROM ejercicios WHERE id_persona = ?', (Id_usuario,))
            series = cursor.fetchall()
            cursor.close()
            for i in range(len(series)):
                series[i] = series[i][0]
            return series
    
    def obtener_descanso_ejercicios(self, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT descanso_series FROM ejercicios WHERE id_persona = ?', (Id_usuario,))
            descanso = cursor.fetchall()
            cursor.close()
            for i in range(len(descanso)):
                descanso[i] = descanso[i][0]
            return descanso
        return []
    
    def obtener_id_ejercicios(self, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT id_ejercicio FROM ejercicios WHERE id_persona = ?', (Id_usuario,))
            id_ejercicio = cursor.fetchall()
            cursor.close()
            for i in range(len(id_ejercicio)):
                id_ejercicio[i] = id_ejercicio[i][0]
            return id_ejercicio
        return []


    def verificar_credenciales(self, email, contraseña):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE email = ? AND contraseña = ?', (email, contraseña)) #buscar un registro en la tabla usuarios donde el email y la contraseña coincidan con los valores proporcionados como argumentos.
            usuario = cursor.fetchone() #fetchone() devuelve una tupla con los datos del usuario
            cursor.close()

            if usuario:
                return True, usuario  # Devuelve True y el registro del usuario
            else:
                return False, None  # Si no se encuentra coincidencia
        return False, None
    
    def crear_tabla_vicios(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS vicio (
            id_vicio INTEGER PRIMARY KEY AUTOINCREMENT,
            id_persona INTEGER NOT NULL,
            nombre_vicio TEXT NOT NULL,
            fecha_dejar DATE NOT NULL,
            compromiso TEXT NOT NULL,
                
            FOREIGN KEY (id_persona) REFERENCES usuarios(id_persona)
            )
            ''')
                
        self.conexion.commit()
        cursor.close()

    def crear_tabla_sentimientos(self):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sentimiento (
                id_sentimiento INTEGER PRIMARY KEY AUTOINCREMENT,
                id_persona INTEGER NOT NULL,
                sentimiento TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                
                FOREIGN KEY (id_persona) REFERENCES usuarios(id_persona)
            )
        ''')
        self.conexion.commit()
        cursor.close()


    def registrar_vicio(self, vicio, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO vicio (id_persona, nombre_vicio, fecha_dejar, compromiso)
                    VALUES (?, ?, ?, ?)
                ''', (Id_usuario, vicio.nombre_vicio, vicio.fecha_dejar, vicio.compromiso))
                self.conexion.commit()
            except sqlite3.Error as error:
                print(f"Error al registrar vicio: {error}")
            finally:
                cursor.close()


    def registrar_sentimiento(self, sentimiento, Id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            try:
                cursor.execute('''
                    INSERT INTO sentimiento (id_persona, sentimiento, descripcion)
                    VALUES (?, ?, ?)
                ''', (Id_usuario, sentimiento.sentimiento, sentimiento.descripcion))
                self.conexion.commit()
            except sqlite3.Error as error:
                print(f"Error al registrar sentimiento: {error}")
            finally:
                cursor.close()            
    

    def obtener_vicios_usuario(self, id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT * FROM vicio WHERE id_persona = ?', (id_usuario,))
            vicios = cursor.fetchall()
            cursor.close()
            return vicios
        return []

    def obtener_sentimientos_usuario(self, id_usuario):
        if self.conexion:
            cursor = self.conexion.cursor()
            cursor.execute('SELECT * FROM sentimiento WHERE id_persona = ?', (id_usuario,))
            sentimientos = cursor.fetchall()
            cursor.close()
            return sentimientos
        return []


    def close(self):
        if self.conexion:
            self.conexion.close()


if __name__ == '__main__':
    db = Database()
    db.connect()
