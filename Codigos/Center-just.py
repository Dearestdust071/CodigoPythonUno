# Archivo que demuestra el uso de "center", "ljust" y "rjust" y sus parametros
# Se crea un string que se usara a lo largo de todo el archivo para demostrar como se usan los metodos
string = "Menu"

# El metodo center ljust y rjust hacen lo mismo con diferentes enfoques:
# center rellena los espacios a la derecha e izquierda del string llenandolo con espacios en blanco
# center rellena los espacios a la derecha del string llenandolo con espacios en blanco
# center rellena los espacios a la izquierda del string llenandolo con espacios en blanco
# Entre los parentesis puedes seleccionar cuantos espacios en blanco se rellanaran 
print("Metodos con espacios: ")
print(string.center(20))
print(string.ljust(20))
print(string.rjust(20))

# Entre los parentesis ademas tambien puedes seleccionar con que se rellenaran los espacios en caso de que quieras usar un caracter por ejemplo
# "=" en este caso
print("\nMetodos con caracter:")
print(string.center(20, "="))
print(string.ljust(20, "="))
print(string.rjust(20, "="))

# Aqui se demuestra el cambiar el parametro de espacios a rellenar usando el metodo center.
print("\nVariable modificada:")
string = string.center(10, "=")
print(string)


