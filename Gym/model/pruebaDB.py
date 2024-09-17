class Usuario:
    
    def __init__(self, nombre: str, id_persona: str, edad: int, email: str, genero: str, fecha_nacimiento: str):
        self.nombre: str = nombre
        self.id_persona: str = id_persona
        self.edad: int = edad
        self.email: str = email
        self.genero: str = genero
        self.fecha_nacimiento: str = fecha_nacimiento


            
    def guardar_informacion(self):
        pass
     
    def cargar_informacion(self):
        pass    