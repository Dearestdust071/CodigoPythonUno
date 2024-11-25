print("CALCULADORA CON UNA VARIABLE \n")

print("*******************")
print("* MENU DE OPCIONES*")
print("*******************")

print("1. SUMA")
print("2. RESTA")
print("3. MULTIPLICACIÓN")
print("4. DIVISIÓN")
print("5. DIVISIÓN ENTERA")
print("6. EXPONENTE")
print("7. MODULO O RESTO \n")

# La siguiente linea permite almacenar un numero entero que el usuario ingrese mediante la terminal y se almacena en la variable numero
numero = int(input("Introduce la opción deseada: "))



# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (+=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero
if numero == 1:
    print ("Elegiste suma \n")
    numero = int(input("Introduce el primer numero: "))
    numero += int(input("Introduce el segundo numero: "))
    print("El resultado de la suma es: ", numero)

elif numero ==2:

# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (-=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero
    print ("Elegiste resta \n")
    numero = int(input("Introduce el primer numero: "))
    numero -= int(input("Introduce el segundo numero: "))
    print("El resultado de la resta es: ", numero)

elif numero ==3:

# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (*=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero
    print ("Elegiste multiplicación \n")
    numero = float(input("Introduce el primer numero: "))
    numero *= float(input("Introduce el segundo numero: "))
    print("El resultado de la multiplicación es: ", numero)


elif numero ==4:
    
# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (/=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero
# En este caso particular se demuestra la diferencia entre float input y int input varian en su funcionamiento debido a que uno permite unicamente numeros enteros (int)
# mientras que el otro permite tambien numeros decimales (float)
    print ("Elegiste división \n")
    numero = float(input("Introduce el primer numero: "))
    numero /= float(input("Introduce el segundo numero: "))
    print("El resultado de la división es: ", numero)


elif numero ==5:
# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (/=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero
# En este caso se usa int en vez de float para devolver un numero redondeado en caso de ser decimal el resultados
    print ("Elegiste división entera \n")
    numero = int(input("Introduce el primer numero: "))
    numero /= int(input("Introduce el segundo numero: "))
    print("El resultado de la división entera es: ", numero)


elif numero ==6:
# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (**=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero en este caso la operacion ** indica que un numero se eleva a cierto otro 
# Tambien se puede usar simplemente ** para elevar un numero a otro
    print ("Elegiste exponente \n")
    numero = int(input("Introduce el primer numero: "))
    numero **= int(input("Introduce el segundo numero: "))
    print("El resultado del exponente es: ", numero)


elif numero ==7:
# Se reutiliza la variable numero para permitir hacer operaciones en ella usando operadores de asignacion (/=) y posterior a eso imprime el resultado 
# almcenado de nuevo en la variable numero
# El modulo calcula el restante de una division de enteros por ejemplo 5/2 (ya que no puede devolver numeros decimales se devuelve 1)
    print ("Elegiste modulo o resto \n")
    numero = int(input("Introduce el primer numero: "))
    numero %= int(input("Introduce el segundo numero: "))
    print("El resultado de modulo o resto es: ", numero)

    
