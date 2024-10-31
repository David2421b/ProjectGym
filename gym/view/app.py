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


app = Flask(__name__)
db = Database()
db.connect()

@dataclass
class Routeapp:     #Esta clase lo que contiene son las diferentes rutas que manejan las diferentes vistas de la aplicacion
    @app.route('/')   #(@app) Define una ruta o URL específica para acceder a una función.
    def home():
        return render_template("Index.html")  

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

    @app.route('/Ejercicio')
    def Ejercicio():
        return render_template("RegisEjercicio.html")
    
    @app.route('/BodyData') 
    def BodyData():
        global Edad, Genero
        return render_template('BodyData.html' , Age = Edad, Gender = Genero)

@dataclass
class Routelogic:  #define las rutas para registrar y autenticar usuarios 
    Nombre = ""
    Edad = 0
    Email = ""
    Contraseña = ""
    Genero = ""

    @app.route('/login', methods=['GET', 'POST']) #GET obtiene datos del servidor y POST envia datos al servidor 
    def login():
        if request.method == 'POST':
            # Obtener los datos del formulario
            email = request.form['email']  # Obtiene el nombre de usuario
            contraseña = request.form['password']  # Obtiene la contraseña

            exito, usuario = db.verificar_credenciales(email, contraseña)

            global Nombre, Edad, Email, Contraseña, Genero, Id_Usr
            
            if exito:  #Autenticacion de informacion de usuario 
                Nombre = usuario[1]  #Se extraen datos del objeto y se asignan a variables globales 
                Edad = usuario[2]
                Email = usuario[3]
                Contraseña = usuario[4]
                Genero = usuario[5]
                Id_Usr = usuario[0]
                return render_template('menu.html', name = Nombre)
            
            else:
                error_message = 'Usuario o contraseña incorrectos'
                return render_template('Index.html', error = error_message)
            

        return render_template('Index.html')  # Si no es un POST, muestra el formulario
    
    @app.route('/MenuName')
    def MenuName():
        global Nombre
        return render_template('menu.html', name = Nombre)


    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':   #Capturan los datos del usuario 
            nombre = request.form['Name']
            edad = request.form['Age']
            email = request.form['Email']
            contraseña = request.form['Password']
            genero = request.form['Gender']
            Dni = request.form['Id']

            usuario = Usuario(nombre, edad, email, contraseña, genero, Dni)  #se crea la instancia usuario 
            db.registrar_usuario(usuario)    #Guardamos informacion en base de datos 
            return render_template('Index.html')
    
        return render_template('Registrarse.html')
    
    @app.route('/EjercicioRegister', methods=['GET', 'POST'])
    def EjercicioRegister():
        global Nombre, Edad, Email, Contraseña, Genero, Id_Usr
        if request.method == 'POST':        #Captura informacion de los ejercicios 
            nombre = request.form['Name']
            tipo = request.form['Type']
            repeticiones = request.form['Reps']
            series = request.form['Series']
            descanso = request.form['Rest']

            ejercicio = Ejercicio(nombre, tipo, repeticiones, series, descanso, Id_Usr)
            db.registrar_ejercicio(ejercicio)  #crea instancia y guarda en base de datos 
            return render_template('menu.html')
    
        return render_template('RegisEjercicio.html')

    @app.route('/UsrData')
    def UsrData():
        global Nombre, Edad, Email, Contraseña, Genero

        return render_template('Usuario.html', Name = Nombre, Age = Edad, Email = Email, Password = Contraseña)


    @app.route('/OllamaChat', methods=['GET', 'POST'])
    def chat():
        if request.method == 'POST':  #propiedad de Flask que indica el método HTTP utilizado para acceder a la ruta 
            mensaje = request.form['message']
            respuesta = Chat_Ollama.chat(mensaje)
            return render_template('Chat.html', mensaje = mensaje, respuesta = respuesta)
        
    
    @app.route('/CalcularData', methods=['GET', 'POST'])
    def CalcularDatas():
        if request.method == 'POST':
            global Edad, Genero
            peso = request.form['Weight']
            altura = request.form['Height']
            IMC = Estadistica.calcular_imc(peso, altura)
            TMB = Estadistica.calcular_tmb(Genero, Edad, peso, altura)
            FCM = Estadistica.calcular_fcm(Edad)
            return render_template('BodyData.html')


        


    
    

if __name__ == '__main__':
    app.run(debug=True)
