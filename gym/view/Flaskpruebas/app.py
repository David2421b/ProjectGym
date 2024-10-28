from flask import *
import time
import sys
import os
sys.path.append("GYM")
from model.DigitalHealth import *
from Logic.DataBase import Database

#   Importatante

#   ANTES DE USAR LA APP RECUERDA QUE DEBES INICIARLA DESDE FLASK Y NO DESDE EL PUERTO 5500 QUE ES CON LIVE SERVER
#   PARA INICIARLA DESDE FLASK DEBES CORRER EL ARCHIVO "app.py" QUE SE ENCUENTRA EN LA RUTA G
#   RECUERDA QUE DEBES INICIAR EL PROGRAMA DE "OLLAMA" PARA QUE EL CHAT FUNCIONE CORRECTAMENTE

#   Hola zungita barata de simon

app = Flask(__name__)
db = Database()
db.connect()

@dataclass
class Routeapp:
    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/menu')
    def menu():
        return render_template("menu.html")

    @app.route('/singup')
    def signup():
        return render_template("Registrarse.html")

    @app.route('/contact')
    def contact():
        return render_template("Contact.html")
    
    @app.route('/chat')
    def Chat():
        return render_template("Chat.html")
    
    @app.route('/Usr')
    def Usr():
        return render_template("Usuario.html")

@dataclass
class Routelogic:
    Nombre = ""
    Edad = 0
    Email = ""
    Contraseña = ""
    Genero = ""

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            # Obtener los datos del formulario
            email = request.form['email']  # Obtiene el nombre de usuario
            contraseña = request.form['password']  # Obtiene la contraseña

            exito, usuario = db.verificar_credenciales(email, contraseña)

            global Nombre 
            global Edad
            global Email
            global Contraseña
            global Genero

            Nombre = usuario[1]
            Edad = usuario[2]
            Email = usuario[3]
            Contraseña = usuario[4]
            Genero = usuario[5]
 
            
            if exito:
                return render_template('menu.html', name = Nombre)
            
            else:
                error_message = 'Usuario o contraseña incorrectos'
                return render_template('index.html', error = error_message)
            

        return render_template('index.html')  # Si no es un POST, muestra el formulario
    
    @app.route('/MenuName')
    def MenuName():
        global Nombre
        return render_template('menu.html', name = Nombre)


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            nombre = request.form['Name']
            edad = request.form['Age']
            email = request.form['Email']
            contraseña = request.form['Password']
            genero = request.form['Gender']
            Dni = request.form['Id']

            usuario = Usuario(nombre, edad, email, contraseña, genero, Dni)
            db.registrar_usuario(usuario)
            return render_template('index.html')
    
    @app.route('/UsrData')
    def UsrData():
        global Nombre
        global Edad
        global Email
        global Contraseña
        global Genero

        return render_template('Usuario.html', Name = Nombre, Age = Edad, Email = Email, Password = Contraseña)


    @app.route('/OllamaChat', methods=['GET', 'POST'])
    def chat():
        if request.method == 'POST':
            mensaje = request.form['message']
            respuesta = Chat_Ollama.chat(mensaje)
            return render_template('Chat.html', mensaje = mensaje, respuesta = respuesta)
        

    @app.route('/BodyData')
    def BodyData():
        return render_template('BodyData.html')
    

if __name__ == '__main__':
    app.run(debug=True)
