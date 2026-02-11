print("Ejercicio 146")
print("")
print("")

def cargarempleado():
    empleados=[]
    for i in range (5):
        nombre=input(f"Introduzca el nombre del empleado {i+1}: ")
        sueldo=int(input(f"Introduzca el sueldo del empleado: {i+1}: "))
        empleados.append((nombre,sueldo))
    return empleados

def imp_emp_sueldo(empleados):
    for nombre, sueldo in empleados:
        print(nombre,sueldo)
    
def sueldomayor(empleados):
    mayor=empleados[0]
    for emp in empleados:
        if emp[1]>mayor[1]:
            mayor=emp
    print(f"El empleado con mayor sueldo es: {mayor[0]}, con un sueldo de: {mayor[1]}€")

def sueldomenor(empleados):
    cant=0
    menor=empleados[0]
    for menor in empleados:
        if menor[1]<1000:
            print(f"El empleado {empleados[cant][0]}, cobra menos de 1000€.")
        cant+=1
    print(f"El total de empleados que cobran menos de 1000€ es: {cant}")


empleados=cargarempleado()
imp_emp_sueldo(empleados)
sueldomayor(empleados)
sueldomenor(empleados)

print("Fin de programa.")



