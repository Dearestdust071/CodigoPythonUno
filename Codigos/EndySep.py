# El parametro end especifica que se anade al final de la impresion
print("esto es un", end="-*/")  # Aqui, en lugar de un salto de linea, se agrega la cadena "-*/" al final
print("ejemplo")  # Esta linea se imprime seguida inmediatamente por "-*/" de la linea anterior (debido a que print de manera automatica da un salto de 
# Linea)

# El parametro sep define el separador entre los argumentos
print("1", "2", "3", "4", "5", sep="-")  # Aqui, los elementos se separan con "-" en lugar del espacio predeterminado