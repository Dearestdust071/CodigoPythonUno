# En este archivo se ven las tuplas:
# Una tupla es una coleccion ordenada e inmutable de datos
# A diferencia de los diccionarios las tuplas solo contienen valores 
# Al ser inmutables no puedes en si modificar los datos de las tuplas
# Solo se puede acceder usando la posiciond e dicho dato con []

# Aqui se crean dos tuplas 
print("***** Usando el operador + ***** \n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Aqui se demuestra como se puede concatenar una tupla
print(f"Tupla1: {tupla1} | tupla2: {tupla2}")
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada, "\n")


# Aqui se demuestra el uso del operador de asignacion += en tuplas 
print("***** Usando el operador += ***** \n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

# Se reutiliza la tupla 1 y a dicha tupla se le agrega la tupla 2
print(f"Tupla1: {tupla1} | tupla2: {tupla2}")
tupla1 += tupla2
print("tupla1: ", tupla1, "\n")



print("***** Usando la funcion tuple() ***** \n")
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

lista = [6, 7, 8, 9, 10]
# Aqui se crea una lista que usando la funcion de tupla se transforma en una tupla y despues se concatena
print(f"Tupla1: {tupla1} | lista: {lista}")
tupla_concatenada = tupla1 + tuple(lista)
print(tupla_concatenada)
