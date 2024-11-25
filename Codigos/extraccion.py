# Mensaje inicial
mensaje = "Hola Ernesto"

# Busca la subcadena "Ernesto" dentro del mensaje
# El método find() devuelve el índice de la primera ocurrencia de la subcadena
# Si no encuentra la subcadena, devuelve -1
buscar_subcadena = mensaje.find("Ernesto")

# Imprime la posición en la que comienza la subcadena encontrada
print(buscar_subcadena)  # Debería devolver el índice 5, ya que "Ernesto" comienza en el índice 5

# Mensaje para la extracción
print("Extraccion: ")

# Extrae una subcadena del mensaje, desde el índice 1 hasta el índice 8 (sin incluir el índice 8)
# Esto dará como resultado la parte "ola Ern"
extraer_cadena = mensaje[1:8]

# Imprime la subcadena extraída
print(extraer_cadena)

# Comparación de cadenas
print("Comparación:")

# Mensajes a comparar
mensaje_uno = "Hola"
mensaje_dos = "Hol"

# Compara si las dos cadenas son iguales
# El operador '==' devuelve True si las cadenas son iguales y False si son diferentes
print(mensaje_uno == mensaje_dos)  # Debería devolver False, ya que "Hola" no es igual a "Hol"