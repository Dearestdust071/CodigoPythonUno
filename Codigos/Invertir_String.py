# Solicita al usuario que ingrese una cadena de texto para invertirla
string = input("Introduce un String para invertirlo: ")

# Inicializa una variable vacía para almacenar la cadena invertida
string_reversed = ""

# Recorre cada carácter de la cadena original
for character in string:
    # Coloca cada carácter al principio de 'string_reversed' para invertir el orden
    string_reversed = character + string_reversed

# Muestra la cadena invertida
print(f"String invertido: {string_reversed}")


