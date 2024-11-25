string = input("Introduce una frase: ")

# Solicita al usuario la palabra que desea eliminar de la frase
palabra = input("Introduce la palabra que deseas eliminar: ")

# Inicializa una variable para almacenar la nueva cadena
substring = ""

# Busca el indice donde aparece la palabra en la frase
indice = string.find(palabra)

# Crea una nueva cadena excluyendo la palabra indicada
# Toma desde el carácter inmediatamente después de la palabra eliminada (indice + len(palabra) + 1) hasta el final de la cadena.
substring = string[0 : indice] + string[indice + len(palabra) + 1 : ]

# Muestra la cadena resultante sin la palabra eliminada
print(f"Cadena resultante: {substring}")