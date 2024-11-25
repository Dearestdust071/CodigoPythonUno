# Programa que demuestra el uso de la instrucción "del" en listas.
# El objetivo es mostrar cómo se pueden eliminar elementos específicos, porciones o toda una lista.

# Ejemplo 1: Eliminar un elemento específico por su índice
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista original: {vocales}")
del vocales[3]  # Eliminar el elemento en la posición 3 (la letra "o")
print(f"Lista después de 'del vocales[3]': {vocales}")

# Ejemplo 2: Eliminar un rango de elementos
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista original: {vocales}")
del vocales[0:2]  # Eliminar los elementos en las posiciones 0 y 1 ("a" y "e")
print(f"Lista después de 'del vocales[0:2]': {vocales}")

# Ejemplo 3: Eliminar todos los elementos de la lista (vaciar la lista)
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista original: {vocales}")
del vocales[:]  # Vaciar la lista eliminando todos los elementos
print(f"Lista después de 'del vocales[:]': {vocales}")

# Ejemplo 4: Eliminar la lista completa
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista original: {vocales}")
del vocales  # Eliminar la lista completamente