# Conjunción (AND)
print("Conjunción (and)")

# Solicita un número entre 2 y 5 (excluyentes)
num_uno = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número", num_uno, "cumple con la condición.")
else:
    print("El número", num_uno, "NO cumple con la condición.")


# Disyunción (OR)
print("\nDisyunción (or)")

# Solicita una respuesta 'si' o 'yes' para cumplir la condición
palabra = input("Para cumplir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.")
else:
    print("La condición NO se ha cumplido.")


# Negación (NOT)
print("\nNegación (not)")

# Solicita un número que debe ser igual a 5
num_uno = int(input("Introduce un número igual a 5: "))

if not num_uno == 5:
    print("El número es diferente de cinco y SI cumple la condición.")
else:
    print("El número es igual a cinco y NO cumple la condición.")