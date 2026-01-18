"""
Crear dos listas paralelas. En la primera ingresar los nombres de empleados y en la segunda los sueldos de cada empleado.
Ingresar por teclado cuando inicia el programa la cantidad de empleados de la empresa.
Borrar luego todos los empleados que tienen un sueldo mayor a 10000 (tanto el sueldo como su nombre)
"""

# Creamos dos listas paralelas:
# 'empleados' guardará los nombres
# 'sueldos' guardará los importes correspondientes
empleados = []
sueldos = []

# Pedimos cuántos empleados tiene la empresa
cant = int(input("Cuantos empleados tiene la empresa:"))

# Cargamos los datos de cada empleado
for x in range(cant):
    nom = input("Ingrese el nombre:")      # Nombre del empleado
    empleados.append(nom)                  # Lo agregamos a la lista de empleados

    su = int(input("Ingrese el importe del sueldo:"))  # Sueldo del empleado
    sueldos.append(su)                                 # Lo agregamos a la lista de sueldos

# Mostramos el listado completo tal como fue ingresado
print("Listado completo de empleados")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])

# Eliminamos empleados cuyo sueldo sea mayor a 10000
posicion = 0
while posicion < len(sueldos):
    # Si el sueldo en la posición actual es mayor a 10000...
    if sueldos[posicion] > 10000:
        # Eliminamos el sueldo y el empleado en esa misma posición
        # IMPORTANTE: no incrementamos 'posicion' porque la lista se achica
        sueldos.pop(posicion)
        empleados.pop(posicion)
    else:
        # Si el sueldo es 10000 o menos, avanzamos a la siguiente posición
        posicion = posicion + 1

# Mostramos el listado filtrado
print("Listado de empleados que cobran 10000 o menos")
for x in range(len(sueldos)):
    print(empleados[x], sueldos[x])
