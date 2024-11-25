# Ejemplo de uso de la función zip() para combinar elementos de diferentes colecciones

# Definimos las colecciones: una tupla de nombres, una lista de edades y un string
names = ("Luis", "Diego", "Andres", "Carlos")  # Tupla de nombres
ages = [15, 30, 26, 12, 40]  # Lista de edades (nota: más elementos que names)
text = "Geekipedia"  # String que actuará como colección de caracteres


print(names)
print(ages) 
print(text) 

# Uso básico de zip() como objeto iterable
print("\nFuncion zip() como iterable: \n")
combination = zip(names, ages, text)  # Crea un generador que empareja elementos de las colecciones
print(combination)  # Muestra la representación del objeto zip (no su contenido)

# Convertir el objeto zip en una lista para visualizar los pares generados
print("\nFuncion zip() con la funcion list(): \n")
combination = list(zip(names, ages, text))  # Convierte el generador a una lista de tuplas
print(combination)  # Muestra la lista resultante con las combinaciones

# Convertir el objeto zip en una tupla para trabajar con datos inmutables
print("\nFuncion zip() con la funcion tuple(): \n")
combination = tuple(zip(names, ages, text))  # Convierte el generador a una tupla de tuplas
print(combination)  # Muestra la tupla resultante con las combinaciones

# Iterar directamente sobre el objeto zip para procesar cada combinación
print("\nFuncion zip() con for: \n")
for name, age, s_text in zip(names, ages, text):  # Itera sobre los pares generados por zip
    print(name, age, s_text)  # Imprime cada combinación de elementos