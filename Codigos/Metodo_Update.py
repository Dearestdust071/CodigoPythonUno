dict_name = {"a": 1,
             "b": 2,
             "c": 3
            }

# Mostramos el diccionario original
print(f"Diccionario original: {dict_name}")

# Usamos update() para agregar las claves 'z' y 'd' al diccionario
# Si la clave ya existe, update() actualizará su valor
dict_name.update({"z": 4, "d": 5})
print(f"Agregando 'z' y 'd': {dict_name}")

# Actualizamos los valores de las claves existentes 'a' y 'b'
# En este caso, 'a' se actualiza a 6 y 'b' a 5
dict_name.update({"a": 6, "b": 5})
print(f"Actualizando 'a' y 'b': {dict_name}")