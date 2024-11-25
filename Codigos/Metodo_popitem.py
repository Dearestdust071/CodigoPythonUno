dictionary = {"a": 1,
               "b": 2,
               "c": 3
               }

print(dictionary)
# popitem() elimina y devuelve el último par clave-valor del diccionario
item = dictionary.popitem()

# Imprimimos el item eliminado, que es una tupla (clave, valor)
print(f"El item eliminado es: {item}")

print(dictionary)
# Mostramos el diccionario después de la eliminación