# Alternativa 1: Usar `format()` con valores en orden
nombre = "Carlos"
edad = 22

# Se usan llaves {} para los marcadores de posición, y los valores se insertan en el orden en que se pasan al `format()`
print("Hola {}, tienes {} años.".format(nombre, edad))  # Los valores se insertan en el orden en que se pasan

# Alternativa 2: Usar `format()` con palabras clave
nombre = "Carlos"
edad = 22

# En lugar de usar el orden, se pasan los valores explícitamente mediante nombres de variables
print("Hola {nombre}, tienes {edad} años.".format(nombre = "Carlos", edad = 22))  # Usamos nombres explícitos para las variables

# Alternativa 3: Usar `format()` con índices
nombre = "Carlos"
edad = 22

# Usamos índices para indicar cuál valor se coloca en cada posición. 0 es el primer valor (edad) y 1 el segundo (nombre)
print("Hola {1}, tienes {0} años.".format(edad, nombre))  # Usamos índices para especificar el orden de los valores