# Ejemplo del uso de append en listas



# Se crea una lista con letras 
print("Agregando un elemento a la lista")
letters = ["a", "b", "c", "d"]

# Se imprime usando f-strings una manera moderna y sofisticada
print(f"La lista: {letters}")
letters.append("e")
print(f"Lista: {letters}")


# Utlizando el metodo "append" se puede y se agrega en el siguiente bloque de codigo tres letras nuevas
print("Agregando tres elementos a la lista")
letters = ["a", "b", "c", "d"]
print(f"La lista: {letters}")
letters.append("e")
letters.append("f")
letters.append("g")
print(f"Lista: {letters}")


# En el siguiente bloque de codigo se puede ver que en las listas se aceptan diferentes tipos de datos y 
# append tambien permite diferentes tipos de datos
print("Agregando tres elementos de distinto tipo de dato a la lista")
letters = ["a", "b", "c", "d"]
print(f"La lista: {letters}")
letters.append(5)
letters.append(2.3)
letters.append(True)
print(f"Lista: {letters}")

