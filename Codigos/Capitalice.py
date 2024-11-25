
# Archivo que demuestra el uso del metodo "capitalize()" 
# Aqui encontramos un string cuyo uso de las minisculas y mayusculas es inadecuado y tiene errores de ortografia
string = "eL VIAJE eS ls RecoMpensa"

print(f"Antes de capitalize (): (${string}))")
# Al utilizar el metodo "capitalize()" el string proveido previamente se transforma en un string cuya unica minuscula sera la primera
string = string.capitalize()
print(f"Despues de capitalice(): (${string})")
