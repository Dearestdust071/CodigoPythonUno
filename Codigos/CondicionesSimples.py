# Sistema para calcular el promedio de un alumno.
# Este programa solicita el nombre del estudiante y sus calificaciones en tres materias.
# Luego calcula el promedio y verifica si el alumno aprobó o no.

# Mostrar mensaje inicial del sistema
print("Sistema para calcular el promedio de un alumno.")

# Solicitar el nombre del alumno
nombre = input("Nombre del Alumno: ")

# Solicitar las calificaciones de las materias. Estas se convierten a enteros para su uso en el cálculo.
matematicas = int(input(nombre + " calificación en matemáticas: "))
quimica = int(input(nombre + " calificación en química: "))
biologia = int(input(nombre + " calificación en biología: "))

# Calcular el promedio de las tres materias
promedio = (matematicas + quimica + biologia) / 3
# Convertir el promedio a entero (redondeo hacia abajo)
promedio = int(promedio)

# Bloque condicional para verificar si el promedio es suficiente para aprobar
if promedio >= 6:
    # Mensaje para estudiantes aprobados
    print('Felicidades ' + nombre + ', "aprobaste" con un promedio de: ', promedio)

# Indicar el final del programa
print("Fin.")