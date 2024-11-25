# Secuencia con lista sin valor asignado
sequence = ["uno", "dos", "tres"]
# Utilizamos `fromkeys()` para crear un diccionario donde las claves provienen de la lista, y el valor es por defecto None
dic_name = dict.fromkeys(sequence)
print("Secuencia con lista sin valor: ", dic_name)

# Secuencia con lista con valor asignado
sequence = ["uno", "dos", "tres"]
value = 5
# Ahora, asignamos un valor específico (5) para todas las claves en el diccionario
dic_name = dict.fromkeys(sequence, value)
print("Secuencia con lista y valor: ", dic_name)

# Secuencia con diccionario
sequence = {"uno": 1,
            "dos": 2,
            "tres": 3
            }

value = 5
# Si la secuencia es un diccionario, las claves del diccionario original son usadas, y el valor asignado es 5
dic_name = dict.fromkeys(sequence, value)
print("Secuencia con diccionario y valor:", dic_name)

# Secuencia con texto
# Convertimos un texto (cadena) en un diccionario donde cada letra es una clave y el valor es 1
dic_name = {}.fromkeys("hola", 1)
print("Secuencia con texto y valor:", dic_name)

# Secuencia con texto y lista
# Similar al caso anterior, pero el valor será una lista [1, 2, "Hola"] para todas las claves
dic_name = {}.fromkeys("hola", [1, 2, "Hola"])
print("Secuencia con texto y valor:", dic_name)

# Secuencia con texto y diccionario
# En este caso, cada letra será una clave y el valor asignado es un diccionario vacío
dic_name = {}.fromkeys("hola", {})
print("Secuencia con texto y valor:", dic_name)