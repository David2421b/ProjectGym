from nicegui import ui
from GYM.model.DigitalHealth import *
from dataclasses import dataclass
from GYM.Logic.DataBase import Database

@dataclass
class Interfaz_inicio:
    #db: ClassVar[Database] = Database()
    #db.conectar()
    #menu(db)

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
                self.registrar_usuario() #habia un db en los parentesis
        elif opcion == "2":
                self.iniciar_sesion() #habia un db en los parentesis
        elif opcion == "3":
            print("Saliendo del programa...")
            #db.close()
        else:
            print("Opción no válida, intenta de nuevo.")
    
    def registrar_usuario():  #habia un db en los parentesis
        pass

    def iniciar_sesion():  #habia un db en los parentesis
        pass


interfaz = Interfaz_inicio()
ui.run()