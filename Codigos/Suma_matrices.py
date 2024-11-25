# Definición de las matrices A y B
matrix_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix_b = [[1, 2, 3],
            [4, 1, 2],
            [1, 1, 0]]

# Creación de una nueva matriz C que almacenará la suma de las matrices A y B
matrix_c = []
for row in range(len(matrix_a)):
    new_row = []
    for column in range(len(matrix_a[0])):
        # Suma de los elementos correspondientes de las matrices A y B
        new_row.append(matrix_a[row][column] + matrix_b[row][column])
    matrix_c.append(new_row)

# Impresión de las matrices y su suma
for row in range(len(matrix_a)):
    if row != 1:
        # Imprimir matrices A, B y C, excluyendo la fila 1 de la forma habitual
        print(f"{matrix_a[row]}  {matrix_b[row]}  {matrix_c[row]}")
    else:
        # Para la fila 1, mostrar la suma explícita de las matrices A y B
        print(f"{matrix_a[row]} + {matrix_b[row]} = {matrix_c[row]}")