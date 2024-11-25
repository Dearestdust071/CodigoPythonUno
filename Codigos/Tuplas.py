# Definición de una tupla vacía
tupla_vacia = ()
print(f"Tupla vacia: {tupla_vacia}")
print(f"El tipo de dato de esta tupla es: {type(tupla_vacia)} \n")

# Definición de una tupla homogénea (con solo números)
tupla_homogenea = (3, 2)
print(f"Tupla homogenea: {tupla_homogenea}")
print(f"El tipo de dato de esta tupla es: {type(tupla_homogenea)} \n")

# Definición de una tupla heterogénea (con diferentes tipos de datos)
tupla_heterogenea = (3, True, "Hola", 2.5)
print(f"Tupla heterogenea: {tupla_heterogenea}")
print(f"El tipo de dato de esta tupla es: {type(tupla_heterogenea)} \n")

# Definición de una tupla heterogénea con estructuras más complejas
tupla_heterogenea2 = ([1, 2, 3], {"uno": 1, "dos": 2}, [])
print(f"Tupla heterogenea2: {tupla_heterogenea2}")
print(f"El tipo de dato de esta tupla es: {type(tupla_heterogenea2)} \n")

# Definición de una tupla con un solo elemento (debe tener una coma al final)
tupla_de_un_elemento = (3, )
print(f"Tupla de un elemento: {tupla_de_un_elemento}")
print(f"El tipo de dato de esta tupla es: {type(tupla_de_un_elemento)} \n")

# Definición de una tupla sin paréntesis (Python permite definir tuplas sin paréntesis)
tupla_sin_parentesis = 3, True, "Hola", 2.5
print(f"Tupla sin paréntesis: {tupla_sin_parentesis}")
print(f"El tipo de dato de esta tupla es: {type(tupla_sin_parentesis)} \n")