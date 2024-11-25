# Definimos un diccionario con claves y valores
dict_name = {"a": 1, 
             "b": 2, 
             "c": 3
            }

# Recorriendo unicamente las claves del diccionario
for key in dict_name:  # El ciclo 'for' itera sobre las claves del diccionario
    # Imprime la clave y su valor correspondiente
    print(f"{key} : {dict_name[key]}")  # 'dict_name[key]' accede al valor de la clave
print()  # Se agrega una línea en blanco para separar las salidas

# Recorriendo tanto las claves como los valores del diccionario
for key, value in dict_name.items():  # 'items()' devuelve una tupla (clave, valor)
    # Imprime la clave y el valor de cada elemento
    print(f"{key} : {value}")