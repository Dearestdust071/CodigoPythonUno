# Definimos un diccionario con frutas y sus precios
fruits_dict = {"manzana": 2.50,
               "platano": 1.75,
               "naranja": 3.00,
               "mango": 4.25
               }

# Imprimimos el diccionario original
print(f"Diccionario original: {fruits_dict}")

# Modificamos el valor asociado a la clave "manzana"
# Cambiamos el precio de la manzana de 2.50 a 3.50
fruits_dict["manzana"] = 3.50
print(f"Diccionario modificado: {fruits_dict}")

# Agregamos una nueva clave "uva" con su precio
# Si la clave no existe, la agrega al diccionario
fruits_dict["uva"] = 4.00
print(f"Nuevo valor agregado: {fruits_dict}")