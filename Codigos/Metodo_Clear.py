# Diccionario de empleados con sus edades y salarios
employees = {"Juan"  : {"edad": 28, "salario": 25000},
             "Maria" : {"edad": 24, "salario": 25000},
              }

# Mostrar el diccionario original
print(f"Diccionario original: {employees}")

# Limpiar el diccionario usando el método clear()
# La función clear() elimina todos los elementos dentro del diccionario
employees.clear()

# Mostrar el diccionario después de ser limpiado
# El diccionario ahora está vacío porque se han eliminado todos sus elementos
print(f"Diccionario actualizado: {employees}")