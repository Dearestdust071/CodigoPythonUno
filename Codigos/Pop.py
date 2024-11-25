# Se crea la lista de vocales y se imprime
vocales = ["a", "e", "i", "o", "u"]
print(f"Lista: {vocales}")
# Elimina el último elemento de la lista y lo imprime
print(f"Elemento eliminado: {vocales.pop()}")
# Imprime la lista después de la eliminación
print(f"Lista: {vocales}")

# Se vuelve a crear la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
# Elimina el elemento en la posición 2 y lo imprime
print(f"Elemento eliminado en la posicion 2: {vocales.pop(2)}")
# Imprime la lista después de la eliminación
print(f"Lista: {vocales}")

# Se vuelve a crear la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
# Elimina el elemento en la posición 0 y lo imprime
print(f"Elemento eliminado en la posicion 0: {vocales.pop(0)}")
# Imprime la lista después de la eliminación
print(f"Lista: {vocales}")

# Se vuelve a crear la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
# Elimina el elemento en la posición -2 (penúltimo) y lo imprime
print(f"Elemento eliminado en la posicion -2: {vocales.pop(-2)}")
# Imprime la lista después de la eliminación
print(f"Lista: {vocales}")

# Se vuelve a crear la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista: {vocales}")
# Intenta eliminar el elemento en la posición 5, lo cual generará un error
print(f"Elemento eliminado en la posicion 5: {vocales.pop(5)}")
# Imprime la lista después de intentar la eliminación (no llegará aquí por el error)
print(f"Lista: {vocales}")