# Inicio del sistema de control vacacional
print("****************************************")
print("*SISTEMA DE CONTROL VACACIONAL DE RAPPI*")
print("****************************************")

# Se solicita información al usuario
nombre_empleado = input("Favor de introducir el nombre del empleado: ")
clave_departamento = int(input("Por favor, introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce los años laborados del empleado: "))

# Evaluamos según la clave del departamento
if clave_departamento == 1:

    # Condiciones de vacaciones para el departamento 1
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 6 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, " tiene derecho a 14 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, " tiene derecho a 20 dias de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a vacaciones.")

elif clave_departamento == 2:

    # Condiciones de vacaciones para el departamento 2
    if antiguedad_empleado == 1 and antiguedad_empleado < 2:
        print("El empleado ", nombre_empleado, " tiene derecho a 7 dias de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <= 6:
        print("El empleado ", nombre_empleado, " tiene derecho a 15 dias de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, " tiene derecho a 22 dias de vacaciones.")
    else:
        print("El empleado ", nombre_empleado, " aún no tiene derecho a vacaciones.")

elif clave_departamento == 3:
    # Condiciones de vacaciones para el departamento 3 (pendiente de implementar)
    pass