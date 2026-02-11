print("Ejercicio 150")
print("")
print("")

def cargadatos():
    nombre=input("Introduce el nombre del empleado: ")
    sueldo=float(input("Introduce el sueldo del empleado: "))
    return (nombre,sueldo)

def sueldomayor(empleado1,empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0] ,"Tiene mayor sueldo.")
    else:
        print(empleado2[0], "Tiene mayor sueldo.")
    


empleado1=cargadatos()
empleado2=cargadatos()
sueldomayor(empleado1, empleado2)

print("Fin de programa")



