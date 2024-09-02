# Definición del problema

En la actualidad, llevar un control detallado de las actividades físicas, rutinas de ejercicios y el seguimiento de la salud personal se ha convertido en una necesidad para muchas personas que buscan mejorar su bienestar. Sin embargo, mantener un registro manual o disperso de estos datos puede ser complicado y poco eficiente. Además, la falta de recordatorios y seguimiento constante puede llevar a la falta de consistencia en las rutinas y al descuido de aspectos importantes de la salud.

El objetivo del proyecto es desarrollar una aplicación que permita a los usuarios gestionar de manera eficiente sus ejercicios y rutinas, así como mantener un historial de sus datos médicos principales. La aplicación también incluirá funcionalidades para enviar mensajes y recordatorios, facilitando así un seguimiento más organizado y personalizado del bienestar físico y de la salud en general.

## Funcionalidad Aplicación

### Gestión de Ejercicios y Rutinas

- Los usuarios podrán crear, modificar y eliminar rutinas de ejercicio.
- La aplicación permitirá llevar un registro detallado de cada rutina, incluyendo tipos de ejercicios, repeticiones, series, y tiempos de descanso.
- Los usuarios podrán marcar la finalización de los ejercicios y recibir recomendaciones basadas en su historial.

### Historial de Datos Médicos

- Los usuarios podrán ingresar y actualizar información médica relevante, como peso, altura, presión arterial, frecuencia cardíaca, etc.
- La aplicación generará reportes para que el usuario pueda visualizar su progreso en términos de salud y condición física.

### Mensajes y Recordatorios

- Los usuarios podrán programar recordatorios personalizados para sus rutinas de ejercicio, citas médicas, y otros aspectos relevantes.
- La aplicación enviará mensajes motivacionales o de alerta para ayudar a los usuarios a mantenerse comprometidos con sus objetivos de salud.

## Interfaz de Usuario

- La aplicación contará con una interfaz amigable y fácil de usar, que permita a los usuarios acceder rápidamente a sus rutinas, historial médico, y configuración de recordatorios.
- Se implementará un sistema de notificaciones para mantener a los usuarios informados y motivados.

## Cálculo de estadísticas

### Índice de Masa Corporal (IMC)

- **Fórmula**: IMC = Peso (kg) / (Altura (m) ^ 2)
- **Descripción**: El IMC es una medida que se utiliza para determinar si una persona tiene un peso saludable en relación con su altura. Los resultados se clasifican en categorías como bajo peso, peso normal, sobrepeso y obesidad.

### Tasa Metabólica Basal (TMB)

- **Fórmula (Harris-Benedict)**:
  - Para hombres: TMB = 88.36 + (13.4 * Peso (kg)) + (4.8 * Altura (cm)) - (5.7 * Edad (años))
  - Para mujeres: TMB = 447.6 + (9.2 * Peso (kg)) + (3.1 * Altura (cm)) - (4.3 * Edad (años))
- **Descripción**: La TMB estima la cantidad de calorías que el cuerpo necesita para mantener funciones vitales en reposo, lo que es útil para planificar dietas y rutinas de ejercicio.

### Frecuencia Cardíaca Máxima y Zonas de Entrenamiento

- **Fórmula**: FCM = 220 - Edad (años)
- **Descripción**: La frecuencia cardíaca máxima se utiliza para definir las zonas de entrenamiento (por ejemplo, quema de grasa, cardio, etc.). Se pueden calcular zonas de frecuencia cardíaca para distintos tipos de ejercicio según un porcentaje de la FCM (50-85%).

### Otras estadísticas

- Presión Arterial Promedio
- Calorías Quemadas durante Ejercicios
- Consumo Máximo de Oxígeno (VO2 Max)
- Control de Glucosa en Sangre
