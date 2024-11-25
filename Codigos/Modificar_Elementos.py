print("Modificando vocales [1] = 'x'")
# Inicializamos la lista de vocales
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos el elemento en la posición 1 (índice 1) de la lista
vocales[1] = 'x'
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [1] = '2'")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos el elemento en la posición 1 (índice 1) de la lista
vocales[1] = '2'
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [-1] = 'x'")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos el último elemento de la lista utilizando el índice negativo -1
vocales[-1] = 'x'
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [2:4] = ['x', 'y']")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos una porción de la lista desde el índice 2 hasta el índice 4 (excluyendo 4)
vocales[2:4] = ['x', 'y']
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [1:3] = ['x', 'y']")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos una porción de la lista desde el índice 1 hasta el índice 3 (excluyendo 3)
vocales[1:3] = ['x', 'y']
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [1:3] = ['x', 'y', 'z']")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos una porción de la lista desde el índice 1 hasta el índice 3 (excluyendo 3) y añadimos más elementos
vocales[1:3] = ['x', 'y', 'z']
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [:2] = ['x', 'y']")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos una porción de la lista desde el inicio hasta el índice 2 (excluyendo 2)
vocales[:2] = ['x', 'y']
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [0:3] = ['x', 'y']")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Modificamos una porción de la lista desde el índice 0 hasta el índice 3 (excluyendo 3)
vocales[0:3] = ['x', 'y']
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [0:3] = 'x', 'y'")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Este bloque está intentando cambiar una porción de la lista de manera incorrecta,
# ya que la asignación de valores múltiples ('x', 'y') no es válida de esta forma.
# Lo corregimos a una lista: ['x', 'y']
vocales[0:3] = ['x', 'y']
print(f"Lista de vocales: {vocales}")

print("Modificando vocales [:] = 'x'")
vocales = ["a", "e", "i", "o", "u"]
print(f"\nLista de vocales: {vocales}")
# Este bloque modifica toda la lista, reemplazando todo el contenido por el valor 'x'.
# Sin embargo, 'x' no es una lista, lo cual generará un error.
# Para hacerlo correctamente, debemos pasar una lista con un solo valor 'x'
vocales[:] = ['x']
print(f"Lista de vocales: {vocales}")