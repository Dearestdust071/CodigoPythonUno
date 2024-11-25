# Diccionario simple con claves 'a' y 'e'
dictionary = {
    "a": 1,
    "e": 2
}

# Imprime el diccionario completo
print(dictionary)

# Accede a los valores de las claves 'a' y 'e'
print(f"Clave a: {dictionary['a']}")
print(f"Clave e: {dictionary['e']}")


print()

# Diccionario con una lista y un diccionario anidado como valores
dictionary = {
    "numbers": [18, 20, 28],
    "groups": {"a": 1, "b": 2}
}

# Imprime el diccionario completo
print(dictionary)

# Accede a la lista completa almacenada en la clave 'numbers'
print(f"Clave numbers: {dictionary['numbers']}")

# Accede al diccionario completo almacenado en la clave 'groups'
print(f"Clave groups: {dictionary['groups']}")

# Accede al segundo elemento de la lista 'numbers' (índice 1)
print(f"Clave numbers: {dictionary['numbers'][1]}")

# Accede al valor correspondiente a la clave 'b' dentro del diccionario 'groups'
print(f"Clave groups: {dictionary['groups']['b']}")

