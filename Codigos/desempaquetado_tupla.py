# Ejemplo de una tupla que contiene nombres de países.
countries_tuple = ("Mexico", "Brasil", "Argentina", "España")
print(countries_tuple, "\n")  # Imprime la tupla completa.

# Desempaquetado de los primeros tres elementos de la tupla.
p1, p2, p3, *_ = countries_tuple  # Se desempaquetan los tres primeros países. El resto (si lo hubiera) se ignora con *_
print(f"Desempaquetado de tupla [0:3]")  # Aviso del rango que se desempaquetará.
print(f"Primer país: {p1}")  
print(f"Segundo país: {p2}") 
print(f"Tercer país: {p3}")  
