from alumno import Alumno
from profesor import Profesor
from comercial import Comercial

def menu():
    print("Menú:\n1. Empleado\n2. Alumno")
    opcion = int(input("Elige una opción: "))

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    if opcion == 1:
        sueldo = float(input("Sueldo: "))
        print("1. Profesor\n2. Comercial")
        tipo = int(input("Elige: "))

        if tipo == 1:
            asignatura = input("Asignatura: ")
            return Profesor(nombre, edad, sueldo, asignatura)
        else:
            comision = float(input("Comisión: "))
            return Comercial(nombre, edad, sueldo, comision)

    elif opcion == 2:
        asignatura = input("Asignatura: ")
        return Alumno(nombre, edad, asignatura)

    else:
        print("Opción no válida")
        return None
