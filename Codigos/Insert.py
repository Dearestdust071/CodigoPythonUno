# Lista original
print("Lista original")
letters = ["b", "d", "f", "g"]
print(f"Lista: {letters}")

# Insertando 'a' en la posición 0
print("\nInsertando 'a' en posicion 0")
letters.insert(0, "a")  # Usando el método insert() para agregar 'a' en la posición 0
print(f"Lista: {letters}")

# Insertando 'c' en la posición 2
print("\nInsertando 'c' en posicion 2")
letters.insert(2, "c")  # Usando el método insert() 
print(f"Lista: {letters}")

# Insertando 'e' en la posición 4
print("\nInsertando 'e' en posicion 4")
letters.insert(4, "e")  # Usando el método insert() 
print(f"Lista: {letters}")

# Intentando insertar 'z' en una posición fuera de rango (esto agregará 'z' al final de la lista)
print("\nInsertando 'z' en posicion 100")
letters.insert(100, "z")  # Insertando 'z' en una posición fuera de rango, lo que resultará en agregarla al final
print(f"Lista: {letters}")