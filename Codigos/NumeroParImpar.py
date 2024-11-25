print("****************************************************")
print("*PROGRAMA QUE DETERMINA SI UN NUMERO ES PAR O IMPAR*")
print("****************************************************")

numero = int(input("Por favor introduce un numero entero: "))

if numero % 2 == 0:
    print(f"El numero {numero} es par.")
else:
    print(f"El numero {numero} es impar.")