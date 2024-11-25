# Definimos una tupla con las vocales
vowels_tuple = ("a", "e", "i", "o", "u")
print(vowels_tuple, "\n")

# Accedemos a un rango de elementos desde la posición 0 hasta la 2 (sin incluir el índice 2)
print(f"Porsiciones [0:2] -> {vowels_tuple[0:2]}")

# Accedemos a los elementos de la tupla con un salto de 2
print(f"Porsiciones [::2] -> {vowels_tuple[::2]}")

# Accedemos a los últimos 3 elementos de la tupla (desde el tercer elemento desde el final)
print(f"Porsiciones [-3:] -> {vowels_tuple[-3:]}")