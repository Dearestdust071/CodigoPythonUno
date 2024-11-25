# Definición de una tupla de tuplas que contiene información sobre frutas.
fruits_tuple = (
    ("001", "Manzana", "rojo"),
    ("002", "Pera", "verde"),
    ("003", "Naranja", "naranja")
)

# Imprime la tupla completa.
print(fruits_tuple, "\n")

# Itera sobre la tupla desempaquetando cada elemento (código, fruta y color).
for code, fruit, color in fruits_tuple:
    # Imprime un mensaje descriptivo sobre cada fruta.
    print(f"La {fruit} tiene el código {code} y es de color {color}.")