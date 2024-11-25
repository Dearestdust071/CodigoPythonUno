# Sistema para calcular el promedio de un alumno.
# Este programa solicita el nombre del estudiante y sus calificaciones en tres materias.
# Luego calcula el promedio y determina si el alumno aprobó o reprobó.

print("Sistema para calcular el promedio de un alumno.")


nombre = input("Nombre del Alumno: ")

# Solicitar las calificaciones de tres materias al alumno y convertirlas a tipo flotante
matematicas = float(input(nombre + ", calificación de matemáticas: "))
quimica = float(input(nombre + ", calificación de química: "))
biologia = float(input(nombre + ", calificación de biología: "))

# Calcular el promedio de las calificaciones usando operadores matematicos
promedio = (matematicas + quimica + biologia) / 3

# Bloque condicional para verificar si el promedio es suficiente para aprobar
if promedio >= 6:
    # Mensaje para estudiantes aprobados
    print('Felicidades, ' + nombre + ' "aprobaste" con un promedio de: ', promedio)
    # Mostrar el promedio redondeado a dos decimales
    print('Felicidades, ' + nombre + ' "aprobaste" con un promedio de: ', round(promedio, 2))
else:
    # Mensaje para estudiantes reprobados
    print('Lo sentimos, ' + nombre + " has 'reprobado' con un promedio de: ", promedio)
    # Mostrar el promedio redondeado a un decimal
    print('Lo sentimos, ' + nombre + " has 'reprobado' con un promedio de: ", round(promedio, 1))

# Indicar el final del programa
print("Fin.")