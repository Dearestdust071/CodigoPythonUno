# Imprimiendo la cadena original con saltos y tabulaciones
cadena = "\tHola Ernesto\n"
print(cadena)

# Eliminando los caracteres específicos de los extremos
cadena = cadena.strip("s tHo\t\n")
print(cadena)