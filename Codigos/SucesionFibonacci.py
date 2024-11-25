# Inicializando los dos primeros números de la secuencia de Fibonacci
num_uno, num_dos = 0, 1

# Mientras el segundo número de la secuencia sea menor o igual a 1597
while num_dos <= 1597:
    # Imprime ambos números
    print(num_uno, num_dos, end=" ")

    # Calcula los siguientes números en la secuencia de Fibonacci
    num_uno = num_uno + num_dos
    num_dos = num_uno + num_dos