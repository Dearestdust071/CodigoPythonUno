print("===================================")
print("¡¡CONVERTIDOR DE NÚMEROS A LETRAS!!")
print("===================================")
# Este código solicita al usuario un número entre 1 y 5 
# y muestra su representación en letras. Si el número 
# ingresado no está en este rango, se informa al usuario.

# Solicitar un número al usuario y convertirlo a entero
num_uno = int(input("¿Cuál es el número que deseas convertir?: "))

# Bloque de condicionales para verificar el valor ingresado y mostrar el resultado
if num_uno == 1:
    print("El número es 'Uno'")
elif num_uno == 2:
    print("El número es 'Dos'")
elif num_uno == 3:
    print("El número es 'Tres'")
elif num_uno == 4:
    print("El número es 'Cuatro'")
elif num_uno == 5:
    print("El número es 'Cinco'")
else:
    # Si el número no está en el rango, se muestra un mensaje de advertencia
    print("Este programa solo puede convertir hasta el número 5")

# Mensaje final para indicar que el programa ha terminado
print("Fin.")