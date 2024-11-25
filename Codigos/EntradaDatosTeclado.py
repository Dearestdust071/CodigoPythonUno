# Se solicita al usuario que ingrese su nombre y se guarda en la variable 'nombre'
nombre = input("¿Cual es tu nombre?: ")

# Muestra un mensaje de bienvenida que incluye el nombre introducido
print("Hola" + nombre + ", vamos a realizar una suma.")

# Se pide al usuario que ingrese el primer número y se convierte a tipo entero (int)
num_uno = int(input("Por favor introduce el primer valor: "))

# Lo mismo
num_dos = int(input("Por favor introduce el segundo valor: "))

# Se realiza la suma de los dos números introducidos por el usuario
resultado = num_uno + num_dos

# Se imprime el resultado de la suma, con un mensaje personalizado utilizando el nombre del usuario
print(nombre + " ,el resultado de la suma es: ", resultado)