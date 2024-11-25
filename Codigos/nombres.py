names_tuple = ("Ana", "Gerardo", "Maria", "Carlos", "Valentina")
print(names_tuple, "\n")

while True:  # Usamos un ciclo infinito y lo rompemos cuando el número sea válido
    try:
        number = int(input("Introduce un numero entero entre 0 y 4: "))  # Intentamos convertir la entrada a entero
        
        if 0 <= number <= 4:  # Verificamos si el número está en el rango correcto
            print(f"El nombre es: {names_tuple[number]}")
            break  # Salimos del ciclo si el número es válido
        else:
            print("¡ERROR! Numero invalido, vuelve a intentarlo. \n")
    
    except ValueError:
        # Si el usuario no ingresa un número válido, capturamos el error
        print("¡ERROR! Debes ingresar un número entero. Vuelve a intentarlo.\n")