# Introduce una frase y una letra con la que terminar el bucle
string = input("Introduce una frase: ")
letter = input("¿Con que frase deseas terminar el bucle?: ")

# Bucle que recorre cada carácter de la cadena
for character in string:
    # Si el carácter es igual a la letra de salida, termina el bucle
    if character.lower() == letter.lower():
        break
    # Si el carácter es una vocal, continúa al siguiente
    elif character.lower() == "a":
        continue
    elif character.lower() == "e":
        continue
    elif character.lower() == "i":
        continue
    elif character.lower() == "o":
        continue
    elif character.lower() == "u":
        continue
    # Imprime el carácter
    print(character, end="")