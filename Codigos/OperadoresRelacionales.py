print("Introduce dos números a comparar:")

# Solicita los dos números
num_uno = int(input("Introduce el primer número: "))
num_dos = int(input("Introduce el segundo número: "))

# Muestra los números que se van a comparar
print("Los números a comparar son:", num_uno, "y", num_dos)

# Compara los dos números en diferentes condiciones
if num_uno == num_dos:
    print("Los números son iguales.")
if num_uno != num_dos:
    print("Los números son diferentes.")
if num_uno < num_dos:
    print(f"{num_uno} es menor que {num_dos}.")
if num_uno > num_dos:
    print(f"{num_uno} es mayor que {num_dos}.")
if num_uno <= num_dos:
    print(f"{num_uno} es menor o igual a {num_dos}.")
if num_uno >= num_dos:
    print(f"{num_uno} es mayor o igual a {num_dos}.")