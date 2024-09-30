from nicegui import *
from GYM.model.DigitalHealth import *
from dataclasses import dataclass
from GYM.Logic.DataBase import Database


@dataclass
class Myapp:

    @ui.page('/')
    def home():
        Interfaz_inicio().menu()
                   
    @ui.page('/registro')
    def registro():
        Interfaz_registro().registrar_usuario()
            
    @ui.page('/chat')
    def chat():
        Interfaz_chat().chat()


@dataclass
class Interfaz_inicio:
    #db: ClassVar[Database] = Database()
    #db.conectar()
    #menu(db)
    inp_opcion: ui.input = None

    def menu(self):
        with ui.column().style("margin-left: 24%; margin-top: 2%"):
            with ui.column().style("display:flex; flex-direction: column; align-items: center;"):
                    ui.label("Bienvenido a la aplicación de DigitalHealth").style("font-size: 40px; color: green; text-align: center;")
                    ui.label("------------------------------------------- MENÚ -------------------------------------------"). style("font-size: 20px; text-align: center; margin-top: 20px; margin-bottom: 20px;")
                    with ui.row():
                        ui.button("Registrar nuevo usuario", on_click = lambda: ui.navigate.to(Myapp.registro)).style("margin-right: 20px;")
                        ui.button("Iniciar Sesion", on_click = lambda: ui.navigate.to("/chat")).style("margin-right: 20px;")
                        ui.button("Chat", on_click = lambda: ui.navigate.to("/chat")).style("margin-right: 20px;")
                        ui.button("Salir", on_click = lambda: print("Saliendo del programa...")).style("margin-right: 20px;")


@dataclass
class Interfaz_registro:

    def registrar_usuario(self):  #habia un db en los parentesis
        inp_name = ui.input("Nombre: ")
        inp_age = ui.input("Edad: ")
        inp_email = ui.input("Email: ")
        inp_password = ui.input("Contraseña: ")
        inp_gender = ui.input("Género: ")
        ui.button("Registrar", on_click = lambda: Database().registrar_usuario(Usuario(inp_name.value, inp_age.value, inp_email.value, inp_password.value, inp_gender.value)))
        ui.button("Volver", on_click = lambda: ui.navigate.back())


@dataclass
class Interfaz_chat:
    with ui.row():
        def chat(self):
            mensaje = ui.input("Cual es tu pregunta: ")
            ui.button("Enviar", on_click = lambda: self.enviar(mensaje.value))
    
    def enviar(self, mensaje):
        respuesta = Chat_Ollama.chat(mensaje)
        ui.label(respuesta)
        

app = Myapp()

ui.run()