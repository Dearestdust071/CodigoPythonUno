string = "Diana se peina sola"
resultado = 0
starts_with = "ejemplos con startswith():"

# Muestra el encabezado con el formato adecuado
print(f"\n{starts_with.rjust(50, 'm')}")

# Comprobación de si la cadena comienza con ciertas subcadenas
resultado = string.startswith("D")
print(f"\n(string) comienza con la subcadena D: {resultado}")

resultado = string.startswith("d")
print(f"\n(string) comienza con la subcadena d: {resultado}")

resultado = string.startswith("Diana")
print(f"\n(string) comienza con la subcadena Diana: {resultado}")

resultado = string.startswith("se")
print(f"\n(string) comienza con la subcadena se, desde la posición 6: {resultado}")

resultado = string.startswith("se", 6)
print(f"\n(string) comienza con la subcadena se, desde la posición 6 hasta la posición 7: {resultado}")

resultado = string.startswith("se", 100)
print(f"\n(string) comienza con la subcadena se, desde la posición 100 hasta la posición 100: {resultado}")

resultado = string.startswith("se", -4, -1)
print(f"\n(string) comienza con la subcadena se, desde la posición -4 hasta la posición -1: {resultado}")

# Muestra el encabezado para el siguiente conjunto de pruebas
print(f"\n{starts_with.rjust(50, '=')}")

# Comprobación de si la cadena termina con ciertas subcadenas
resultado = string.endswith("A")
print(f"\n(string) termina con la subcadena A: {resultado}")

resultado = string.endswith("a")
print(f"\n(string) termina con la subcadena a: {resultado}")

resultado = string.endswith("sola")
print(f"\n(string) termina con la subcadena sola: {resultado}")

resultado = string.endswith("sola", 10)
print(f"\n(string) termina con la subcadena sola, desde la posición 10: {resultado}")

resultado = string.endswith("s", 9, 14)
print(f"\n(string) termina con la subcadena s, desde la posición 9 hasta la posición 14: {resultado}")

resultado = string.endswith("s", 100, 100)
print(f"\n(string) termina con la subcadena s, desde la posición 100 hasta la posición 100: {resultado}")

resultado = string.endswith("s", -4, -2)
print(f"\n(string) termina con la subcadena s, desde la posición -4 hasta la posición -2: {resultado}")