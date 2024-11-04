import csv

# Definir los datos de la tabla
datos = [
    ['ID', 'Nombre', 'Edad', 'Email'],
    [1, 'Juan Perez', 30, 'juan.perez@example.com'],
    [2, 'Maria Gomez', 25, 'maria.gomez@example.com'],
    [3, 'Carlos Ruiz', 35, 'carlos.ruiz@example.com']
]

# Crear un archivo CSV y escribir los datos
with open('usuarios.csv', 'w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(datos)

print("Tabla creada en usuarios.csv")
