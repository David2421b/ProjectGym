import sys
import os

from nicegui import *
from dataclasses import dataclass

sys.path.append("GYM")
from model.DigitalHealth import *
from Logic.DataBase import Database


@dataclass
class Myapp:

    @ui.page('/')
    def home():
        Interfaz_inicio().menu()
    
    @ui.page('/inicio_sesion')
    def inicio_sesion():
        Interfaz_inicio_sesion().iniciar_sesion()
                   
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
        ui.add_head_html("""
                        <style> 
                            body{
                                background-color: #2E2E2E;
                                font-family: Arial, sans-serif;}
                         </style>""")
                      
        
        with ui.column().style("margin-left: 24%; margin-top: 2%"):
            with ui.column().style("display:flex; flex-direction: column; align-items: center;"):
                    ui.label("Bienvenido a la aplicación de DigitalHealth").style("font-size: 40px; color: #FF0000; text-align: center; margin-bottom: 20px;")
                    ui.button("Registrar nuevo usuario", color = '#FF6F20', on_click = lambda: ui.navigate.to(Myapp.registro)).style("margin-right: 20px;")
                    ui.button("Iniciar Sesion", color = '#FF6F20', on_click = lambda: ui.navigate.to("/inicio_sesion")).style("margin-right: 20px;")


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
class Interfaz_inicio_sesion:
    
    def iniciar_sesion(self):

        ui.add_head_html("""
                    <style> 
                        body{
                            background-image: url('https://mrwallpaper.com/images/hd/download-fitness-wallpaper-idil3ryz1gr63bcl.jpg');
                            background-size: cover;
                            background-repeat: no-repeat;
                    </style>""")

        with ui.card().style("width: 300px; margin: 0 auto; margin-top: 10%;"):
            ui.input("Email: ").style("margin-bottom: 10px; width: 100%;")
            ui.input("Contraseña: ").style("margin-bottom: 10px; width: 100%;")
            ui.button("Iniciar Sesion", on_click = self.submit).style("width: 100%; margin-bottom: 10px;")
    
    def submit(self):
        print("Iniciando sesion...")


@dataclass
class Interfaz_chat:
    with ui.row():
        def chat(self):
            mensaje = ui.input("Cual es tu pregunta: ")
            ui.button("Enviar", on_click = lambda: self.enviar(mensaje.value))
    
    def enviar(self, mensaje):
        respuesta = Chat_Ollama.chat(mensaje)
        ui.label(respuesta)


@dataclass
class Interfaz_funciones:
        
    def funciones(self):
        ui.button("Chat", color = '#FF6F20', on_click = lambda: ui.navigate.to("/chat")).style("margin-right: 20px;")
        ui.button("Salir", color = '#FF6F20', on_click = lambda: print("Saliendo del programa...")).style("margin-right: 20px;")

        

app = Myapp()

ui.run()