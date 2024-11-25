#Ejemplo para break 

print("while con la sentencia break")
# El siguiente bloque de codigo inicializa un while que aumenta el contador en uno por cada cuelta que se de mientras que el contador sea menor que 10
contador = 0
while contador <10:
    contador += 1
# Sin embargo si el contador llega a 5 el siguiente bloque de codigo detendra de manera abrupta el while sin importar el while
    if contador == 5:
        break



    print("Valor actual de la variable: ", contador)


print("Fin del programa, la sentencia break se ha ejecutado")





#Ejemplo para continue

# El siguiente bloque de codigo inicializa un while que aumenta el contador en uno por cada cuelta que se de mientras que el contador sea menor que 10
print("while con la sentencia continue")
contador = 0
while contador <10:
    contador += 1

    # El siguiente bloque de codigo con continue hace que se detenga la iteracion actual del while y salte a la siguiente sin detener todo
    if contador == 5:
        continue

    print("Valor actual de la variable: ", contador)
    
