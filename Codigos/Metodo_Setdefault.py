dict_name = {"manzana": 2,
               "platano": 3,
               "naranja": 1
               }

# Mostramos el diccionario original
print(f"{dict_name} \n")

# Intentamos agregar una clave que ya existe en el diccionario
# La función setdefault() retorna el valor actual de la clave si existe, 
# y no modifica el diccionario si ya tiene la clave
return_value = dict_name.setdefault("platano", 4)
print(f"El valor retornado de ('platano', 4) es: {return_value}")
print(f"El diccionario actualizado es: {dict_name}\n")

# Intentamos agregar una clave que no existe en el diccionario sin valor
# setdefault() agregará la clave con el valor None si no se proporciona un valor
return_value = dict_name.setdefault("kiwi")
print(f"El valor retornado de ('kiwi') es: {return_value}")
print(f"El diccionario actualizado es: {dict_name}\n")

# Intentamos agregar una clave que no existe en el diccionario con un valor
# setdefault() agregará la clave con el valor especificado si no existe
return_value = dict_name.setdefault("mango", 5)
print(f"El valor retornado de ('mango', 5) es: {return_value}")
print(f"El diccionario actualizado es: {dict_name}\n")