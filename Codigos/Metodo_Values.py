dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }

# Mostrar el diccionario original
print(dictionary)

# Mostrar los valores del diccionario usando .values()
print(f"\nLos valores del diccionario son: \n{dictionary.values()}")

# Convertir los valores del diccionario a una lista utilizando el constructor list()
print("\nConvirtiendo los valores a lista utilizando el contructor list()")
list_values = list(dictionary.values())

# Mostrar la lista de valores
print(f"La lista es: {list_values}")

# Mostrar el valor en la posición 1 de la lista
print(f"Posicion 1 de la lista values: {list_values[1]}")