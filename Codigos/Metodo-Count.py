string = "mi mamá me mima"
contador = 0

# Centrar la cadena en un espacio de 40 caracteres y agregar "=" como relleno
print(string.center(40, "="))

# Contar cuántas veces aparece la letra "M" (mayúscula) en la cadena
contador = string.count("M")
print(f"\nLa letra M se encontró {contador} vecs en la cadena: {string}")

# Contar cuántas veces aparece la letra "m" (minúscula) en la cadena
contador = string.count("m")
print(f"\nLa letra m se encontró {contador} vecs en la cadena: {string}")

# Contar cuántas veces aparece la secuencia de caracteres "mamá" en la cadena
contador = string.count("mamá")
print(f"\nLa letra mamá se encontró {contador} vecs en la cadena: {string}")

# Contar cuántas veces aparece la secuencia "me mima" en la cadena
contador = string.count("me mima")
print(f"\nLa letra me mima se encontró {contador} vecs en la cadena: {string}")

# Contar cuántas veces aparece la secuencia "ma" en la cadena
contador = string.count("ma")
print(f"\nLa letra ma se encontró {contador} vecs en la cadena: {string}")

# Contar cuántas veces aparece la letra "m" desde la posición 13 en adelante
contador = string.count("m", 13)
print(f"\nLa letra m se encontró {contador}, desde la posicion 13 en la cadena: {string}")

# Intentar contar cuántas veces aparece la letra "m" desde una posición mayor que la longitud de la cadena
contador = string.count("m", 100)
print(f"\nLa letra m se encontró {contador}, desde la posicion 100 en la cadena: {string}")

# Contar cuántas veces aparece la letra "m" desde la posición -3 (posición relativa desde el final)
contador = string.count("m", -3)
print(f"\nLa letra m se encontró {contador}, desde la posicion -3 en la cadena: {string}")

# Contar cuántas veces aparece la letra "m" desde la posición 3 en adelante
contador = string.count("m", 3)
print(f"\nLa letra m se encontró {contador}, desde la posicion 3 en la cadena: {string}")

# Intentar contar cuántas veces aparece la letra "m" desde una posición mayor que la longitud de la cadena
contador = string.count("m", 100)
print(f"\nLa letra m se encontró {contador}, desde la posicion 100 en la cadena: {string}")

# Contar cuántas veces aparece la letra "m" desde la posición -4 (posición relativa desde el final)
contador = string.count("m", -4)
print(f"\nLa letra m se encontró {contador}, desde la posicion -4 en la cadena: {string}")