print("*******************************************************")
print("*PROGRAMA PARA DETERMINAR EL NUMERO MAS GRANDE DE TRES*")
print("*******************************************************")

# Pedimos los tres números al usuario
num_uno = int(input("Introduce el primer numero: "))
num_dos = int(input("Introduce el segundo numero: "))
num_tres = int(input("Introduce el tercer numero: "))

# Usamos la función max() para encontrar el número más grande
numero_mas_grande = max(num_uno, num_dos, num_tres)

print(f"El numero {numero_mas_grande} es el numero mas grande de los tres.")