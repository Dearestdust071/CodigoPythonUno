dict_name = {"a": 1,
               "b": 2,
               "c": 3
               }

print(f"Diccionario Original: {dict_name}")
# Usamos pop() para eliminar la clave 'b' y almacenar su valor
last_value = dict_name.pop("b")

print(f"Diccionario Modificado: {dict_name}")
# Imprimimos el valor que fue eliminado
print(f"Valor Eliminado: {last_value}")

print()

dict_name = {"a": 1,
               "b": 2,
               "c": 3
               }

print(f"Diccionario Original: {dict_name}")
# Intentamos eliminar una clave 'z' que no existe. Si no se encuentra, se usa el valor por defecto
last_value = dict_name.pop("z", "No se encuentra la clave dentro del diccionario.")

print(f"Diccionario Modificado: {dict_name}")
# Imprimimos el valor eliminado o el mensaje por defecto si no se encontró la clave
print(f"Valor Eliminado: {last_value}")