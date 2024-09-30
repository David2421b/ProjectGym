from nicegui import *
from GYM.model.DigitalHealth import *
from dataclasses import dataclass
from GYM.Logic.DataBase import Database

@dataclass
class Myapp:
     
     def create_routes(self):
          
        @ui.page('/')
        def home(self):
            Interfaz_inicio.menu()
            
            
        @ui.page('/registro')
        def registro(self):
            Interfaz_registro.registrar_usuario()
            
        @ui.page('/chat')
        def chat(self):
            pass


@dataclass
class Interfaz_inicio:
    #db: ClassVar[Database] = Database()
    #db.conectar()
    #menu(db)
    inp_opcion: ui.input = None

    def __post_init__(self):
         self.menu()

    def menu(self):
        with ui.column().style("display:flex; flex-direction: column; align-items: center;"):
                ui.label("Bienvenido a la aplicación de DigitalHealth").style("font-size: 40px; color: green; text-align: center;")
                ui.label("------------------------------------------- MENÚ -------------------------------------------"). style("font-size: 20px; text-align: center; margin-top: 20px; margin-bottom: 20px;")
                ui.label("opción '1' para Registrar nuevo usuario")
                ui.label("opción '2' para Iniciar sesión")
                ui.label("opción '3' para Salir \n")
                self.inp_opcion = ui.input("Selecciona una opción: ")
                ui.button("Enviar", on_click = self.procesar_opcion)

    def procesar_opcion(self):
        opcion = self.inp_opcion.value

        if opcion == "1":
            lambda: ui.open("/registro")

        elif opcion == "2":
                pass
        
        elif opcion == "3":
            print("Saliendo del programa...")
            #db.close()

        else:
            print("Opción no válida, intenta de nuevo.")

@dataclass
class Interfaz_registro:

    def registrar_usuario(self):  #habia un db en los parentesis
        inp_name = ui.input("Nombre: ")
        inp_age = ui.input("Edad: ")
        inp_email = ui.input("Email: ")
        inp_password = ui.input("Contraseña: ")
        inp_gender = ui.input("Género: ")


def interfaz_registro():
    interfaz_2 = Interfaz_registro()
    ui.run()

interfaz_1 = Interfaz_inicio()
ui.run()