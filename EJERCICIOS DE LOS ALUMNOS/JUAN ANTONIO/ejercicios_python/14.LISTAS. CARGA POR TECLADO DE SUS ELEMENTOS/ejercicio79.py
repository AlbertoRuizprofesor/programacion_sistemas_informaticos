"""
Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) 
Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.
Imprimir las dos listas de sueldos.
"""

sueldosMañana = []                     #Lista vacía para guardar los sueldos del turno de mañana

print("Sueldos turno mañana")
for x in range(4):                     #Repetimos 4 veces (4 empleados)
    valor = float(input("Ingrese sueldo: "))   # Pedimos un sueldo y lo convertimos a float
    sueldosMañana.append(valor)                # Guardamos el sueldo en la lista de mañana

sueldosTarde = []                      #Lista vacía para los sueldos del turno de tarde

print("Sueldos turno tarde")
for x in range(4):                     #Repetimos 4 veces (4 empleados)
    valor = float(input("Ingrese sueldo: "))   #Pedimos un sueldo
    sueldosTarde.append(valor)                 #Lo añadimos a la lista de tarde

print("Turno mañana")
print(sueldosMañana)                   #Mostramos la lista completa de sueldos de la mañana

print("Turno tarde")
print(sueldosTarde)                    #Mostramos la lista completa de sueldos de la tarde
