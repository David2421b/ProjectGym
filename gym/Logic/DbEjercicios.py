import sqlite3
import os


class DbEjercicios:
    def __init__(self, name_db='DbEjercicios.db'):
        self.name_db = os.path.join(os.path.dirname(__file__), 'database', name_db)
        self.conexion = None


    def connect(self):
        try:
            conexion = sqlite3.connect(self.name_db, check_same_thread=False)
            self.crear_tabla_ejercicios()

        except sqlite3.Error as err:
            self.conexion = None


