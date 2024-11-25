# Diccionario vacío
dictionary_empty = {}

# Imprime el diccionario vacío
print(f"Diccionario vacío: {dictionary_empty}")
print()

# Diccionario homogéneo (todos los valores son del mismo tipo)
dictionary_ages = {
    "Juan": 32,
    "Gerardo": 21,
    "Luis": 25
}

# Imprime el diccionario con edades
print(f"Diccionario de edades: {dictionary_ages}")
print()

# Diccionario heterogéneo (los valores tienen tipos de datos diferentes)
dictionary_dates = {
    "name": "Brenda",
    "last_name": "Flores",
    "age": 22
}

# Imprime el diccionario heterogéneo
print(f"Diccionario con datos variados: {dictionary_dates}")
print()

# Un diccionario que almacena listas y otros diccionarios como valores
dictionary_list = {
    "a": {"a": 1},  # Valor es otro diccionario
    "b": [0, 1, 2]  # Valor es una lista
}

# Imprime el diccionario que contiene una lista y un diccionario como valores
print(f"Diccionario con lista y diccionario: {dictionary_list}")