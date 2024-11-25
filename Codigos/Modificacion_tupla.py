# Definimos la tupla original
nums_tuple = (5, 8, 3, 3, 1, 6, 2)
print(f"Tupla original: {nums_tuple} \n")

# Solicitar al usuario que ingrese el número a modificar por 0
num = int(input("¿Cual de esos numeros quieres modificar por 0?"))

# Convertimos la tupla en una lista para poder modificarla
nums_tuple = list(nums_tuple)

# Obtenemos la longitud de la lista para poder recorrerla
len_tuple = len(nums_tuple)

# Recorremos la lista por índice
for index in range(len_tuple):
    # Si el número de la lista es igual al que ingresó el usuario, lo modificamos
    if nums_tuple[index] == num:
        nums_tuple[index] = 0

# Convertimos de nuevo la lista modificada a una tupla
nums_tuple = tuple(nums_tuple)

# Imprimimos la tupla modificada
print(f"\nTupla modificada: {nums_tuple} \n")