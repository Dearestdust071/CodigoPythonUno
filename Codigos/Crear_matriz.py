# Programa para crear y mostrar una matriz bidimensional.
# Este programa solicita al usuario las dimensiones de la matriz y sus elementos, 
# y luego imprime la matriz completa.

# Solicitar el número de filas para la matriz
rows = int(input("¿Cuántas filas tendrá la matriz?: "))

# Solicitar el número de columnas para la matriz
columns = int(input("¿Cuántas columnas tendrá la matriz?: "))

# Inicializar una lista vacía para almacenar la matriz
matrix = []

# Construcción de la matriz mediante un ciclo anidado
for row_position in range(rows):
    # Crear una lista temporal para almacenar los elementos de la fila actual
    row = []
    for element in range(columns):
        # Solicitar al usuario un valor entero para agregar a la fila actual
        row.append(int(input(f"Introduce un elemento para la fila {row_position}, columna {element}: ")))
    # Agregar la fila completa a la matriz
    matrix.append(row)

# Mostrar la matriz fila por fila
for row in matrix:
    print(row)