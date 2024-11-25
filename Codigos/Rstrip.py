# Se crea una cadena con espacios en blanco y salto de línea al final
cadena ="\tHola Ernesto\n"
print(cadena)

# Elimina los caracteres "s", " ", "t", "H", "o", tabulaciones y saltos de línea al final de la cadena
cadena = cadena.rstrip("s tHo\t\n")
print(cadena)

# Se crea la misma cadena inicial
cadena ="\tHola Ernesto\n"
print(cadena)

# Elimina los caracteres "s", " ", "t", "H", "o", tabulaciones y saltos de línea al principio de la cadena
cadena = cadena.lstrip("s tHo\t\n")
print(cadena)