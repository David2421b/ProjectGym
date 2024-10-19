from flask import *
import sys
import os
sys.path.append("GYM")
from model.DigitalHealth import *
from Logic.DataBase import Database


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']  # Obtiene el nombre de usuario
        password = request.form['password']  # Obtiene la contraseña
        
        # Aquí puedes agregar la lógica para verificar el usuario (por ejemplo, comprobar en una base de datos)
        if username == 'a' and password == 'a':  # Ejemplo simple de verificación
            return redirect(url_for("menu"))  # Redirige al menu si el inicio de sesión es exitoso
        else:
            return "Usuario o contraseña incorrectos", 401  # Manejo de errores para credenciales incorrectas

    return render_template('login.html')  # Si no es un POST, muestra el formulario


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']


if __name__ == '__main__':
    app.run(debug=True)
