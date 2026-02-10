# Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

turnomañana = []
turnotarde = []

for empleado in range(4):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    turnomañana.append(sueldo)

for empleado in range(4):
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    turnotarde.append(sueldo)

print(f"Los sueldos de la manana son: {turnomañana}")
print(f"Los sueldos de la tarde son: {turnotarde}")