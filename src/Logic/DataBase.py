import mysql.connector
from DigitalHealth import Usuario  # Importamos la clase Usuario desde otro archivo

class Database:
    def __init__(self, host='localhost', user='root', password='', database='digital_health'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def connect(self):
        try:
            self.conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Conexión exitosa")
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")

    def close(self):
        if self.conexion and self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada")

    def get_cursor(self):
        if self.conexion:
            return self.conexion.cursor()
        return None

    def registrar_usuario(self, usuario: Usuario):
        cursor = self.get_cursor()
        if cursor:
            try:
                sql = """
                INSERT INTO usuarios (nombre, edad, email, contraseña, genero)
                VALUES (%s, %s, %s, %s, %s)
                """
                valores = (usuario.nombre, usuario.edad, usuario.email, usuario.contraseña, usuario.genero)
                cursor.execute(sql, valores)
                self.conexion.commit()
                print(f"Usuario {usuario.nombre} insertado correctamente en la base de datos.")
            except mysql.connector.Error as error:
                print(f"Error al insertar en la base de datos: {error}")
            finally:
                cursor.close()

    def verificar_credenciales(self, email: str, contraseña: str):
        cursor = self.get_cursor()
        if cursor:
            try:
                sql = """
                SELECT * FROM usuarios WHERE email = %s AND contraseña = %s
                """
                valores = (email, contraseña)
                cursor.execute(sql, valores)
                resultado = cursor.fetchone()
                if resultado:
                    print("Bienvenido!")
                else:
                    print("Credenciales incorrectas.")
            except mysql.connector.Error as error:
                print(f"Error al verificar credenciales: {error}")
            finally:
                cursor.close()