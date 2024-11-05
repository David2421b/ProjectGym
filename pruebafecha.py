from datetime import datetime
from datetime import datetime

# Fecha del suceso (año, mes, día)
fecha_suceso = datetime(2023, 1, 1)  # Cambia esta fecha por la de tu suceso

# Fecha actual
fecha_actual = datetime.now()

# Calcular la diferencia en días
diferencia = fecha_actual - fecha_suceso
dias_pasados = diferencia.days

print(f"Han pasado {dias_pasados} días desde el suceso.")
