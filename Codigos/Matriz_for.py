# Matriz con bucles for

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Mostrar todos los elementos de la matriz fila por fila
print("Mostrar todos los elementos de la matriz fila por fila")
for row in matrix:
    print(row)

# Mostrar todos los elementos de la matriz a elemento en columna
print("Mostrar todos los elementos de la matriz a elemento en columna")
for row in matrix:
    for element in row:
        print(element)

# Mostrar todos los elementos de la matriz en formato de matriz
print("Mostrar todos los elementos de la matriz en formato de matriz")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()