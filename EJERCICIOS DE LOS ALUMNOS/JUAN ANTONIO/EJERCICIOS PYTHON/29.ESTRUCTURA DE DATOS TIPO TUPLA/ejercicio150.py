"""
Confeccionar un programa con las siguientes funciones:
1) Cargar el nombre de un empleado y su sueldo. Retornar una tupla con dichos valores
2) Una función que reciba como parámetro dos tuplas con los nombres y sueldos de empleados
 y muestre el nombre del empleado con sueldo mayor. 
En el bloque principal del programa llamar dos veces a la función de carga y seguidamente 
llamar a la función que muestra el nombre de empleado con sueldo mayor.
"""

# -----------------------------------------
# Función: ingresar_empleado
# Solicita el nombre y el sueldo de un empleado.
# Devuelve una tupla con (nombre, sueldo).
# -----------------------------------------

def ingresar_empleado():
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    sueldo_empleado = float(input("Ingrese su sueldo: "))
    return (nombre_empleado, sueldo_empleado)


# -----------------------------------------
# Función: comparar_sueldos
# Recibe dos tuplas con datos de empleados.
# Cada tupla tiene la forma (nombre, sueldo).
# Compara los sueldos y muestra quién gana más.
# -----------------------------------------

def comparar_sueldos(emp1, emp2):
    if emp1[1] > emp2[1]:                     # Compara los sueldos
        print(emp1[0], "tiene mayor sueldo")  # emp1[0] = nombre
    else:
        print(emp2[0], "tiene mayor sueldo")  # emp2[0] = nombre


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

empleado_a = ingresar_empleado()              # Carga datos del primer empleado
empleado_b = ingresar_empleado()              # Carga datos del segundo empleado

comparar_sueldos(empleado_a, empleado_b)      # Determina quién gana más
