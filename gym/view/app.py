from flask import *
from datetime import *
import time
import sys
import os
sys.path.append("GYM")
from model.DigitalHealth import *
from Logic.DataBase import Database
from flask import Flask, render_template, request
import sqlite3

 
#   Importatante

#   ANTES DE USAR LA APP RECUERDA QUE DEBES INICIARLA DESDE FLASK Y NO DESDE EL PUERTO 5500 QUE ES CON LIVE SERVER
#   PARA INICIARLA DESDE FLASK DEBES CORRER EL ARCHIVO "app.py" QUE SE ENCUENTRA EN LA RUTA G
#   RECUERDA QUE DEBES INICIAR EL PROGRAMA DE "OLLAMA" PARA QUE EL CHAT FUNCIONE CORRECTAMENTE


app = Flask(__name__)
db = Database()  
db.connect()


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


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

    @app.route('/Vicios')
    def Vicios():
        return render_template('ManejoVicios.html')
    
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
        if Nombre == "":  #verifica si la variable esta vacia 
            return render_template('Index.html')   #si nombre esta vacio rederige al usuario a la pagina
        return render_template('menu.html', name = Nombre)  #si el nombre no esta vacio se asume que ya se inicio


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

            ejercicio = Ejercicio(nombre, tipo, repeticiones, series, descanso)
            Database.DNIUsr(Id_Usr)
            db.registrar_ejercicio(ejercicio)  #crea instancia y guarda en base de datos 
            return render_template('menu.html')
    
        return render_template('RegisEjercicio.html')
    
    @app.route('/ver_ejercicios')
    def ver_ejercicios():

        global Id_Usr
        db.connect() 
        ejercicios = db.obtener_todos_ejercicios(Id_Usr)
        id = db.obtener_id_ejercicios(Id_Usr)
        nombre = db.obtener_nombres_ejercicios(Id_Usr)
        tipo = db.obtener_tipo_ejercicios(Id_Usr)
        repeticiones = db.obtener_repeticiones_ejercicios(Id_Usr)
        series = db.obtener_series_ejercicios(Id_Usr)
        descanso = db.obtener_descanso_ejercicios(Id_Usr)
        count = 0
        for i in range(len(ejercicios)):
            count += 1

        if count == 0:

            return render_template('NoData.html')
        elif count == 1:
            return render_template('DashBoardData.html',
                               Id1 = id[0],
                               Nombre1 = nombre[0],
                               Tipo1 = tipo[0],
                               Repeticiones1 = repeticiones[0],
                               Series1 = series[0],
                               Descanso1 = descanso[0])
        
        elif count == 2:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1],
                               Nombre1 = nombre[0], Nombre2 = nombre[1],
                               Tipo1 = tipo[0], Tipo2 = tipo[1],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1],
                               Series1 = series[0], Series2 = series[1],
                               Descanso1 = descanso[0], Descanso2 = descanso[1])
        
        elif count == 3:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1], Id3 = id[2],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2])
        
        elif count == 4:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3])

        elif count == 5:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3], Id5 = id[4],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3], Nombre5 = nombre[4],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3], Tipo5 = tipo[4],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3], Repeticiones5 = repeticiones[4],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3], Series5 = series[4],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3], Descanso5 = descanso[4])

        elif count == 6:
            return render_template('DashBoardData.html',
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3], Id5 = id[4], Id6 = id[5],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3], Nombre5 = nombre[4], Nombre6 = nombre[5],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3], Tipo5 = tipo[4], Tipo6 = tipo[5],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3], Repeticiones5 = repeticiones[4], Repeticiones6 = repeticiones[5],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3], Series5 = series[4], Series6 = series[5],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3], Descanso5 = descanso[4], Descanso6 = descanso[5])

        elif count == 7:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3], Id5 = id[4], Id6 = id[5], Id7 = id[6],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3], Nombre5 = nombre[4], Nombre6 = nombre[5], Nombre7 = nombre[6],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3], Tipo5 = tipo[4], Tipo6 = tipo[5], Tipo7 = tipo[6],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3], Repeticiones5 = repeticiones[4], Repeticiones6 = repeticiones[5], Repeticiones7 = repeticiones[6],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3], Series5 = series[4], Series6 = series[5], Series7 = series[6],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3], Descanso5 = descanso[4], Descanso6 = descanso[5], Descanso7 = descanso[6])

        elif count == 8:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3], Id5 = id[4], Id6 = id[5], Id7 = id[6], Id8 = id[7],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3], Nombre5 = nombre[4], Nombre6 = nombre[5], Nombre7 = nombre[6], Nombre8 = nombre[7],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3], Tipo5 = tipo[4], Tipo6 = tipo[5], Tipo7 = tipo[6], Tipo8 = tipo[7],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3], Repeticiones5 = repeticiones[4], Repeticiones6 = repeticiones[5], Repeticiones7 = repeticiones[6], Repeticiones8 = repeticiones[7],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3], Series5 = series[4], Series6 = series[5], Series7 = series[6], Series8 = series[7],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3], Descanso5 = descanso[4], Descanso6 = descanso[5], Descanso7 = descanso[6], Descanso8 = descanso[7])

        elif count == 9:
            return render_template('DashBoardData.html',
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3], Id5 = id[4], Id6 = id[5], Id7 = id[6], Id8 = id[7], Id9 = id[8], 
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3], Nombre5 = nombre[4], Nombre6 = nombre[5], Nombre7 = nombre[6], Nombre8 = nombre[7], Nombre9 = nombre[8],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3], Tipo5 = tipo[4], Tipo6 = tipo[5], Tipo7 = tipo[6], Tipo8 = tipo[7], Tipo9 = tipo[8],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3], Repeticiones5 = repeticiones[4], Repeticiones6 = repeticiones[5], Repeticiones7 = repeticiones[6], Repeticiones8 = repeticiones[7], Repeticiones9 = repeticiones[8],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3], Series5 = series[4], Series6 = series[5], Series7 = series[6], Series8 = series[7], Series9 = series[8],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3], Descanso5 = descanso[4], Descanso6 = descanso[5], Descanso7 = descanso[6], Descanso8 = descanso[7], Descanso9 = descanso[8])

        elif count == 10:
            return render_template('DashBoardData.html', 
                               Id1 = id[0], Id2 = id[1], Id3 = id[2], Id4 = id[3], Id5 = id[4], Id6 = id[5], Id7 = id[6], Id8 = id[7], Id9 = id[8], Id10 = id[9],
                               Nombre1 = nombre[0], Nombre2 = nombre[1], Nombre3 = nombre[2], Nombre4 = nombre[3], Nombre5 = nombre[4], Nombre6 = nombre[5], Nombre7 = nombre[6], Nombre8 = nombre[7], Nombre9 = nombre[8], Nombre10 = nombre[9],
                               Tipo1 = tipo[0], Tipo2 = tipo[1], Tipo3 = tipo[2], Tipo4 = tipo[3], Tipo5 = tipo[4], Tipo6 = tipo[5], Tipo7 = tipo[6], Tipo8 = tipo[7], Tipo9 = tipo[8], Tipo10 = tipo[9],
                               Repeticiones1 = repeticiones[0], Repeticiones2 = repeticiones[1], Repeticiones3 = repeticiones[2], Repeticiones4 = repeticiones[3], Repeticiones5 = repeticiones[4], Repeticiones6 = repeticiones[5], Repeticiones7 = repeticiones[6], Repeticiones8 = repeticiones[7], Repeticiones9 = repeticiones[8], Repeticiones10 = repeticiones[9],
                               Series1 = series[0], Series2 = series[1], Series3 = series[2], Series4 = series[3], Series5 = series[4], Series6 = series[5], Series7 = series[6], Series8 = series[7], Series9 = series[8], Series10 = series[9],
                               Descanso1 = descanso[0], Descanso2 = descanso[1], Descanso3 = descanso[2], Descanso4 = descanso[3], Descanso5 = descanso[4], Descanso6 = descanso[5], Descanso7 = descanso[6], Descanso8 = descanso[7], Descanso9 = descanso[8], Descanso10 = descanso[9])    

    @app.route('/Rutinas')
    def Rutinas():
        return render_template('DashBoardRutinas.html')

    @app.route('/AgregarEjerLista', methods=['GET', 'POST'])
    def AgregarEjerLista():
        if request.method == 'POST':
            global Id_Usr, Nombre
            RutinaName = request.form['Name']
            id1 = request.form['Id_Vicio1']
            id2 = request.form['Id_Vicio2']
            id3 = request.form['Id_Vicio3']
            id4 = request.form['Id_Vicio4']
            id5 = request.form['Id_Vicio5']
            rutina = Rutinas(RutinaName, id1, id2, id3, id4, id5)
            db.registrar_rutina(rutina, Id_Usr)
            return render_template('Menu.html' , Name = Nombre)

    @app.route('/UsrData')
    def UsrData():
        global Nombre, Edad, Email, Contraseña, Genero
        return render_template('Usuario.html', Name = Nombre, Age = Edad, Email = Email, Password = Contraseña)


    @app.route('/OllamaChat', methods=['GET', 'POST'])
    def chat():
        if request.method == 'POST':  #propiedad de Flask que indica el método HTTP utilizado para acceder a la ruta 
            mensaje = request.form['message'] #Accedemos al diccionario que contiene los datos
            respuesta = Chat_Ollama.chat(mensaje)
            return render_template('Chat.html', mensaje = mensaje, respuesta = respuesta)
        
    
    @app.route('/CalcularData', methods=['GET', 'POST'])
    def CalcularDatas():
        if request.method == 'POST':
            global Edad, Genero
            peso = int(request.form['Weight'])
            altura = float(request.form['Height'])
            peso = peso  / 100
            IMC = Estadistica.calcular_imc(peso, altura)
            TMB = Estadistica.calcular_tmb(Genero, Edad, peso, altura)
            FCM = Estadistica.calcular_fcm(Edad)
            return render_template('BodyData.html', Imc = IMC, Tmb = TMB, Fcm = FCM)
         

    @app.route('/Vicios_Name')
    def Vicios_Name():
        global Nombre
        return render_template('ManejoVicios.html', Name = Nombre)
     

    @app.route('/ViciosData', methods=['GET','POST'])
    def registrar_vicio():
        if request.method == 'POST':
            global Nombre, Id_Usr
            nombre_vicio = request.form['vicio']
            fecha_dejar = request.form['Fecha']
            compromiso = request.form['compromiso']
            vicio = Vicio(nombre_vicio, fecha_dejar, compromiso)
            db.registrar_vicio(vicio, Id_Usr)
            return render_template('ManejoVicios.html', Name = Nombre)  # Redirige a una página de éxito


    @app.route('/registrar_sentimiento', methods=['GET', 'POST'])
    def registrar_sentimiento():
        if request.method == 'POST':
            global Id_Usr
            sentimiento = request.form['sentimiento']
            descripcion = request.form['descripcion']
            sentimiento_obj = Sentimiento(sentimiento, descripcion)
            db.registrar_sentimiento(sentimiento_obj, Id_Usr)
            return render_template('ManejoVicios.html')

    
if __name__ == '__main__':
    app.run(debug=True)

