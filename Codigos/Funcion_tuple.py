# Ejemplo 1 - Crear una coordenada con tuple ()
print("***** Ejemplo 1 ***** \n")
x = 10  # Coordenada x
y = 5   # Coordenada y

coordenada = tuple([x, y])  # Creamos una tupla con x e y
print(f"La tupla es: {coordenada} \n")


# Ejemplo 2 - Convertir un String a tupla
print("***** Ejemplo 2 ***** \n")
string = input("Introduce un String: ")  # Pedimos un texto al usuario

string_tuple = tuple(string)  # Convertimos el string en una tupla de caracteres
print(f"La tupla es: {string_tuple} \n")


# Ejemplo 3 - Convertir un diccionario a tupla (claves)
print("***** Ejemplo 3 ***** \n")
numbers_dict = {"uno": 1, "dos": 2, "tres": 3}  # Diccionario con claves y valores

numbers_tuple = tuple(numbers_dict)  # Convertimos solo las claves a tupla
print(f"La tupla es : {numbers_tuple} \n")


# Ejemplo 4 - Convertir un diccionario a tupla (valores)
print("***** Ejemplo 4 ***** \n")
numbers_dict = {"uno": 1, "dos": 2, "tres": 3}  # Reutilizamos el diccionario

numbers_tuple = tuple(numbers_dict.values())  # Convertimos solo los valores a tupla
print(f"La tupla es : {numbers_tuple} \n")