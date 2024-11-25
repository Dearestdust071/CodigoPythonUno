# Se crea la lista de vocales y se imprime
vocales = ["a", "e", "i", "o", "u"]
print(f"{vocales} \nElemento a eliminar: i")
# Elimina la primera aparición de "i" y imprime la lista actualizada
vocales.remove("i")
print(vocales)

# Se vuelve a crear la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"{vocales} \nElemento a eliminar: o")
# Elimina la primera aparición de "o" y imprime la lista actualizada
vocales.remove("o")
print(vocales)

# Se vuelve a crear la lista de vocales con dos "i"
vocales = ["a", "e", "i", "o", "i"]
print(f"{vocales} \nElemento a eliminar: i")
# Elimina la primera aparición de "i" y imprime la lista actualizada
vocales.remove("i")
print(vocales)

# Se vuelve a crear la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"{vocales} \nElemento a eliminar: I")
# Intenta eliminar "I", pero no existe, lo que generará un error
vocales.remove("I")
print(vocales)