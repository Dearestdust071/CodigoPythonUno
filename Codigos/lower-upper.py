# Lower y Upper

string = input("Introduce un String: ")

# Comprobando si todas las letras están en minúsculas
print(f"\n¿Todas las letras estan en minusculas?: {string.islower()}")
string_lower = string.lower()
print(f"String en minusculas: {string_lower}")

# Comprobando si todas las letras están en mayúsculas
print(f"\n¿Todas las letras estan en mayusculas?: {string.isupper()}")
string_upper = string.upper()
print(f"String en mayusculas: {string_upper}")
print(f"String original: {string}")