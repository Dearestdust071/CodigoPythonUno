print("\nEjercicio #4")

# Diccionario con frutas y sus respectivas cantidades
fruits = {
    "manzanas": 5,
    "peras": 2,
    "naranjas": 4
}

# Imprime el diccionario completo
print(fruits)

# Verifica si la clave "manzanas" existe en el diccionario
print(f"La clave manzanas existe en el diccionario?:")

# Condicional para comprobar si "manzanas" está en el diccionario
if "manzanas" in fruits:
    print(True)  # Si la clave existe, imprime True
else:
    print(False)  # Si la clave no existe, imprime False