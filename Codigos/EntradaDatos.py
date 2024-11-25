# Este archivo solicita al usuario ingresar diferentes tipos de datos: 
# una cadena, un entero, un flotante y un numero complejo. Luego imprime cada uno de ellos con su respectivo tipo.

# Solicita una palabra y la almacena como cadena en la variable palabra
palabra = input("Introduce una palabra: ")

# Solicita un numero entero, lo convierte a entero y lo almacena en la variable num_int
num_int = int(input("Introduce un numero entero: "))

# Solicita un numero flotante, lo convierte a flotante y lo almacena en la variable num_float
num_float = float(input("Introduce un numero flotante: "))

# Solicita un numero complejo, lo convierte a complejo y lo almacena en la variable num_complex
# Numeros matematicos cabrones
num_complex = complex(input("Introduce un numero complejo: "))

# Imprime la palabra ingresada
print("string: ", palabra)

# Imprime el numero entero ingresado
print("Entero: ", num_int)

# Imprime el numero flotante ingresado
print("Flotante: ", num_float)

# Imprime el numero complejo ingresado
print("Numero Complejo: ", num_complex)