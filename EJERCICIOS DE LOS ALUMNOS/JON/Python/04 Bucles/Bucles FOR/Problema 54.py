print("Problema 54")
print("")
print("")

suma_m=0
suma_t=0
suma_n=0
print("Introduzca la edad de los 5 alumnos de la mañana: ")
for i in range(5):
    edad_m=int(input("Edad del alumno de mañana: "))
    suma_m=suma_m+edad_m
promedio_m=suma_m/5
print("El promedio de edad de los alumnos de la mañana es: ", promedio_m)
for i in range(6):
    edad_t=int(input("Edad del alumno de la tarde: "))
    suma_t=suma_t+edad_t
promedio_t=suma_t/6
print("El promedio de edad de todos los alumnos es: ", promedio_t)
for i in range(11):
    edad_n=int(input("Edad del alumno de noche: "))
    suma_n=suma_n+edad_n
promedio_n=suma_n/11
print("El promedio de edad de los alumnos de la noche es: ", promedio_n)
if promedio_m>promedio_t and promedio_m>promedio_n:
    print("El grupo con mayor promedio de edad es el de la mañana")
if promedio_t>promedio_m and promedio_t>promedio_n:
    print("El grupo con mayor promedio de edad es el de la tarde")
if promedio_n>promedio_m and promedio_n>promedio_t:
    print("El grupo con mayor promedio de edad es el de la noche")
    