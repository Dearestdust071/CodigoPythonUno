# Concatenando cadenas de texto
mensaje = "Hola"
mensaje += " "
mensaje += "Ernesto"
print(mensaje)

print("concatenación")

# Concatenando utilizando variables
mensaje = "Hola"
espacio = " "
nombre = "ernesto"
print(mensaje + espacio + nombre)

# Suma de números convertida a cadena
numero_uno = 4
numero_dos = 6
resultado = numero_uno + numero_dos
resultado = str(resultado)
print("El resultado de la suma es: " + resultado)

print("Busqueda: ")
# Buscando la posición de una subcadena en un string
mensaje = "Hola Ernesto"
buscar_subcadena = mensaje.find("Ernesto")
print(buscar_subcadena)