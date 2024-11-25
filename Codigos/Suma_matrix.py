number_of_matrix = int(input("¿Cuántas matrices quieres sumar?: "))

if number_of_matrix > 1:

    rows = int(input("¿Cuántas filas tendrán las matrices?: "))
    columns = int(input("¿Cuántas columnas tendrán las matrices?: "))

    matrix_list = []

    # Llenado de matrices
    for number in range(number_of_matrix):
        matrix = []
        for row in range(rows):
            new_row = []
            for column in range(columns):
                new_row.append(
                    int(input(f"Introduce un elemento para la matriz {number + 1} fila {row}, columna {column}: ")))
            matrix.append(new_row)
        matrix_list.append(matrix)

    # Suma de las matrices
    result_matrix = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            sum_matrix = 0
            for matrix_position in range(len(matrix_list)):
                sum_matrix += matrix_list[matrix_position][row][column]
            new_row.append(sum_matrix)  # Arreglado el error aquí
        result_matrix.append(new_row)

    # Imprimir matrices y su suma
    print("\nLas matrices y su suma son:")
    for matrix_row in range(rows):
        for matrix_list_position in range(len(matrix_list)):
            if matrix_list_position != len(matrix_list) - 1:
                print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" + ")
            else:
                print(f"{matrix_list[matrix_list_position][matrix_row]}", end=" = ")
        print(f"{result_matrix[matrix_row]}")  # Imprimir la fila de la matriz resultado

else:
    print("Se necesitan dos o más matrices para realizar la suma.")