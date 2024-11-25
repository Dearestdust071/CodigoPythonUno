fruits_dict = {"manzana": 1.55,
               "platano": 3.55,
               "naranja": 1.25
               }

print(fruits_dict)

# Obtener el precio de la manzana usando get()
precio_manzana = fruits_dict.get("manzana")
print(f"El precio de la manzana es: {precio_manzana}")

# Intentar obtener el precio del mango, que no existe en el diccionario
precio_mango = fruits_dict.get("mango")
print(f"El precio del mango es: {precio_mango}")

# Usar get() con un valor por defecto, en caso de que la clave no exista
precio_mango = fruits_dict.get("mango", 4.55)
print(f"El precio del mango es: {precio_mango}")