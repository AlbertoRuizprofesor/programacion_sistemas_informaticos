print("Ejercicio 153")
print("")
print("")

def cargarempleados():
    empleados=[]
    for i in range (5):
        nombre=input(f"Introduce el nombre del empleado {i+1}: ")
        s1=float(input(f"Introduce el último sueldo del empleado {i+1}: "))
        s2=float(input(f"Introduce el penúltimo sueldo del empleado {i+1}: "))
        s3=float(input(f"Introduce el antepenúltimo sueldo del empleado {i+1}: "))
        empleados.append([nombre,(s1,s2,s3)])
    return empleados

def imprimirsueldos(empleados):
    print("El sueldo de los empleados es: ")
    for x in range (5):
        totalingresos=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        print(f"Empleado: {empleados[x][0]} , ha ingresado: {totalingresos} ")
    
def ingresomayor(empleados):
    for x in range (5):
        totalingresos=empleados[x][1][0]+empleados[x][1][1]+empleados[x][1][2]
        if totalingresos>10000:
            print(f"El empleado {empleados[x][0]} ha ingresado más de 10.000€")

empleados=cargarempleados()
imprimirsueldos(empleados)
ingresomayor(empleados)

print("Fin del programa")
