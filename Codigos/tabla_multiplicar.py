# Se solicita al usuario que ingrese el número de la tabla de multiplicar que desea ver
num = int(input("¿Que tabola de multiplicar quieres ver?:"))

# Se imprime un encabezado indicando la tabla de multiplicar seleccionada
print(f"La tabla de multiplicar del {num} es: ")

# Se genera un ciclo para mostrar las multiplicaciones del número elegido
for i in range(11):
    # Se imprime cada multiplicación en el formato adecuado
    print(f"{num} x {i} = {num * i} ")