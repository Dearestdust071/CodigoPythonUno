string = input("Ingresa un texto:")

# Crea un diccionario donde cada letra del texto es una clave, 
# y el valor inicial de cada letra es 0
letters = dict.fromkeys(string, 0)

# Recorre cada letra del texto ingresado
for letter in string:
    # Incrementa el contador de la letra en el diccionario
    letters[letter] += 1

# Imprime el diccionario final con la cantidad de veces que aparece cada letra
print(letters)