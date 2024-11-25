# Accediendo a las posiciones de una lista
marcas = ["Apple", "Samsung", "Xiami", "Huawei"]

# Se imprime la lista completa
print(f"\nLista completa: {marcas}")

# Se muestra cuántos elementos tiene la lista utilizando la función len()
print(f"\n¿Cuantos elementos tiene la lista? - len(marcas): {len(marcas)}")

# Se accede al segundo elemento de la lista (índice 1)
print(f"\nmarcas[1]: {marcas[1]}")

# Se accede al cuarto elemento de la lista (índice 3)
print(f"\nmarcas[3]: {marcas[3]}")

# Se accede al último elemento de la lista usando índice negativo
print(f"\nmarcas[-1]: {marcas[-1]}")

# Se accede al tercer elemento desde el final (índice -3)
print(f"\nmarcas[-3]: {marcas[-3]}")

# Se accede a un subconjunto de la lista, desde el índice 1 hasta el índice 3 (sin incluirlo)
print(f"\nmarcas[1:3]: {marcas[1:3]}")

# Se accede a los primeros dos elementos de la lista
print(f"\nmarcas[:2]: {marcas[:2]}")

# Se accede a todos los elementos de la lista desde el índice 1 hasta el final
print(f"\nmarcas[1:]: {marcas[1:]}")

# Se accede a todos los elementos de la lista (copia completa)
print(f"\nmarcas[:]: {marcas[:]}")

# Imprime la lista completa otra vez para confirmación
print(marcas) 

# Generación de un error al intentar acceder a un índice fuera del rango
print(f"Generando error - {marcas[4]}")