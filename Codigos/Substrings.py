# Definiendo la cadena principal
string = "012346789"
substring = ""

# Mostrando la cadena principal
print(f"Cadena principal: {string}")

# Accediendo a la subcadena con índice en la posición [0]
substring = string[0]
print(f"\nSubcadena con índice en la posición [0] es: {substring}")

# Accediendo a la subcadena con índice en la posición [5]
substring = string[5]
print(f"\nSubcadena con índice en la posición [5] es: {substring}")

# Accediendo a la subcadena con índice en la posición [-4]
substring = string[-4]
print(f"\nSubcadena con índice en la posición [-4] es: {substring}")

# Accediendo a la subcadena con índice en la posición [0:3]
substring = string[0:3]
print(f"\nSubcadena con índice en la posición [0:3] es: {substring}")

# Accediendo a la subcadena con índice en la posición [:3]
substring = string[:3]
print(f"\nSubcadena con índice en la posición [:3] es: {substring}")

# Accediendo a la subcadena con índice en la posición [5:]
substring = string[5:]
print(f"\nSubcadena con índice en la posición [5:] es: {substring}")

# Accediendo a la subcadena con índice en la posición [-4:-1]
substring = string[-4:-1]
print(f"\nSubcadena con índice en la posición [-4:-1] es: {substring}")

# Accediendo a la subcadena completa
substring = string[:]
print(f"\nSubcadena con índice en la posición [:] es: {substring}")

# Accediendo a la subcadena con índice y salto [1:6:2]
substring = string[1:6:2]
print(f"\nSubcadena con índice en la posición y salto [1:6:2] es: {substring}")

# Accediendo a la subcadena con índice y salto [::3]
substring = string[::3]
print(f"\nSubcadena con índice en la posición y salto [::3] es: {substring}")