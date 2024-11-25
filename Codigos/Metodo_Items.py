dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }

print(dictionary)
print(f"\nLos items del diccionario son:\n{dictionary.items()}")

# Convertir los items del diccionario a una lista usando el constructor list()
print("\nConvirtiendo items a lista utilizando el constructor list()")
list_items = list(dictionary.items())

print(f"La lista es: {list_items}")
print(f"La posición 1 de la lista items: {list_items[1]}")