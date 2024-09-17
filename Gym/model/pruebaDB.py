import mysql.connector

class Usuario:
    def __init__(self, nombre: str, edad: int, email: str, contraseña: str, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.contraseña = contraseña
        self.genero = genero

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

# Funciones fuera de las clases
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

# Configuración de la base de datos y ejecución del menú
db = Database()
db.connect()
menu(db)

