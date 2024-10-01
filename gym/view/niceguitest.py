import sys
import os

from nicegui import *
from dataclasses import dataclass


sys.path.append("GYM")
from GYM.model.DigitalHealth import *
from GYM.Logic.DataBase import Database


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
    
    @ui.page('/funciones')
    def funciones():
        Interfaz_funciones().funciones()
            
    @ui.page('/chat')
    def chat():
        Interfaz_chat().chat()


@dataclass
class Interfaz_inicio:
    #db: ClassVar[Database] = Database()
    #db.conectar()
    #menu(db)

    def menu(self):
        ui.add_head_html("""
                        <style> 
                            body{
                                background-color: #2E2E2E;
                                font-family: Arial, sans-serif;}
                         </style>""")
                      
        
        with ui.column().style("margin: 0 auto; margin-top: 2%"):
            with ui.column().style("display:flex; flex-direction: column; align-items: center;"):
                    ui.label("Bienvenido a la aplicación de DigitalHealth").style("font-size: 40px; color: #FF0000; text-align: center; margin-bottom: 20px;")
                    ui.button("Registrar nuevo usuario", color = '#FF6F20', on_click = lambda: ui.navigate.to(Myapp.registro)).style("margin-right: 20px;")
                    ui.button("Iniciar Sesion", color = '#FF6F20', on_click = lambda: ui.navigate.to("/inicio_sesion")).style("margin-right: 20px;")


@dataclass
class Interfaz_registro:

    def registrar_usuario(self):  #habia un db en los parentesis
        with ui.card().style("width: 300px; margin: 0 auto; margin-top: 5%;"):
            inp_name = ui.input("Nombre: ").style("margin-bottom: 10px; width: 100%;")
            inp_age = ui.input("Edad: ").style("margin-bottom: 10px; width: 100%;")
            inp_email = ui.input("Email: ").style("margin-bottom: 10px; width: 100%;")
            inp_password = ui.input("Contraseña: ").style("margin-bottom: 10px; width: 100%;")
            inp_gender = ui.input("Género: ").style("margin-bottom: 10px; width: 100%;")
            ui.button("Registrar", on_click = lambda: Database().registrar_usuario(Usuario(inp_name.value, inp_age.value, inp_email.value, inp_password.value, inp_gender.value))).style("margin-bottom: 10px; width: 100%;")
            ui.button("Volver", on_click = lambda: ui.navigate.back()).style("margin-bottom: 10px; width: 100%;")


@dataclass
class Interfaz_inicio_sesion:
    
    def iniciar_sesion(self):

        ui.add_head_html("""
                    <style> 
                        body{
                            background-image: url("https://mrwallpaper.com/images/hd/download-fitness-wallpaper-idil3ryz1gr63bcl.jpg");
                            background-size: cover;
                            background-repeat: no-repeat;
                    </style>""")

        with ui.card().style("width: 300px; margin: 0 auto; margin-top: 10%;"):
            email_inp = ui.input("Email: ").style("margin-bottom: 10px; width: 100%;")
            password_inp = ui.input("Contraseña: ").style("margin-bottom: 10px; width: 100%;")
            ui.button("Iniciar Sesion", on_click = self.submit).style("width: 100%; margin-bottom: 10px;")
    
    def submit(self):
        if True:
            ui.navigate.to("/funciones")


@dataclass
class Interfaz_chat:
    
    def chat(self):
        mensaje = ui.input("Cual es tu pregunta: ").style("margin-bottom: 10px; width: 100%;")
        ui.button("Enviar", on_click = lambda: self.enviar(mensaje.value)).style("margin-bottom: 10px; width: 100%;")
    
    def enviar(self, mensaje):
        respuesta = Chat_Ollama.chat(mensaje)
        ui.label(respuesta)



@dataclass
class Interfaz_funciones:
        
    def funciones(self):
        with ui.row().style("margin: 0 auto; margin-top: 2%;"): 
            ui.button("Chat", color = '#FF6F20', on_click = lambda: ui.navigate.to("/chat")).style("margin-right: 20px;")
            ui.button("Medidas", color = '#FF6F20', on_click = lambda: print("IMC")).style("margin-right: 20px;")
        
        ui.button("Salir", color = '#FF6F20', on_click = lambda: print("Saliendo del programa...")).style("margin-right: 20px;")

        

app = Myapp()
ui.run()