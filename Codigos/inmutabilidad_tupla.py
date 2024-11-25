# Intento de reasignación de un elemento directo en una tupla - Esto generaría un error ya que las tuplas son inmutables.
"""
nums_tuple = (1, 2, 3, 4, 5)
nums_tuple[0] = 5
"""

# Ejemplo de una tupla que contiene objetos mutables.
"""
info_tuple = ([1, 2, 3], {"uno"; 1, "dos": 2}, (3, 2))
info_tuple[0] = 2  # Esto también fallaría porque no se puede reasignar un elemento completo de la tupla.
"""

# Tupla que contiene una lista, un diccionario y otra tupla. Aunque no se pueden modificar los elementos directamente,
# sí se pueden cambiar los valores internos de los objetos mutables dentro de la tupla.

info_tuple = ([1, 2, 3], {"uno": 1, "dos": 2}, (3, 2))  
print(f"Tupla original: {info_tuple}")

# Modificando el segundo elemento de la lista contenida en la tupla.
info_tuple[0][1] = 99
print(f"Tupla[0][1]: {info_tuple} \n")

# Modificando el valor asociado a la clave 'dos' en el diccionario contenido en la tupla.
info_tuple[1]['dos'] = 88
print(f"Tupla[1]['dos']: {info_tuple} \n")