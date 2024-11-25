# Ejemplo 1
# Se imprime una cadena, pero la expresión (4+1) no se evalúa dentro del f-string
# Para que funcione correctamente, se debe colocar la expresión entre llaves {} para evaluarla.
print(f"El resultado de la suma de 4+1 es: {4+1}")

# Ejemplo 2
nombre = "Carlos"
estatura = 1.80
edad = 22

# El f-string permite incluir variables dentro de la cadena utilizando las llaves {}
# En este caso se mostrarán las variables 'nombre', 'edad' y 'estatura'
print(f"Hola {nombre}, tienes {edad} años y mides {estatura} metros")

# Ejemplo 3
# Solicita al usuario ingresar su nombre y dos números para realizar una suma
nombre = input("¿Cuál es tu nombre? ")
num_uno = int(input("Introduce un número: "))
num_dos = int(input("Introduce un segundo número: "))

# En este caso, las variables 'nombre', 'num_uno', y 'num_dos' son incluidas en el f-string para mostrar un mensaje
print(f"Hola {nombre}, el resultado de {num_uno} + {num_dos} es: {num_uno + num_dos}")