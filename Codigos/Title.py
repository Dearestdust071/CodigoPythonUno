# Se piden los datos del nombre y apellido
first_name = input("Nombre: ")
last_name = input("Apellido: ")

# Se forma el nombre completo con el formato f-string
full_name = f"{first_name} {last_name}"

print()

# Se imprime si el formato de title() se ha aplicado en el nombre completo
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}")

# Se aplica el método title() para mostrar el nombre con la primera letra en mayúscula
print(f"Aplicando el metodo title(): {full_name.title()}")

# Se imprime el nombre original para ver cómo estaba antes de aplicar title()
print(f"Volvemos a imprimir el nombre: {full_name}")

print()

# Se aplica title() permanentemente al nombre completo
full_name = full_name.title()

# Se verifica si el formato ahora está en title case
print(f"¿El formato del metodo title() se ha aplicado?: {full_name.istitle()}")

# Se imprime el nombre completo después de aplicar title()
print(f"Se ha aplicado el metodo title() de manera permanente: {full_name}")