#Ejercicio 79: Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas.Imprimir las dos listas de sueldos.

Mañana=[]
print("Sueldos turno de mañana")

for i in range(4):
    sueldo1=float(input(f"Introduce su sueldo {i+1} (Horario de mañana): "))
    Mañana.append(sueldo1)
    
    
    
    
Tarde=[]
print("Sueldos turno de tarde")

for i in range(4):
    sueldo2=float(input(f"Introduce su sueldo {i+1} (Horario de tarde): "))
    Tarde.append(sueldo2)
    
print("Turno mañana")
print(Mañana)
print("Turno tarde")
print(Tarde)