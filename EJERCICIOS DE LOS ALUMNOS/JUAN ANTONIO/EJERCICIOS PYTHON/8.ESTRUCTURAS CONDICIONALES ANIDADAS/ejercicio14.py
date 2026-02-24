#Confeccionar un programa que pida por teclado tres notas de un alumno, calcule el promedio e imprima alguno de estos mensajes:
#Si el promedio es >=7 mostrar "Promocionado".
#Si el promedio es >=4 y <7 mostrar "Regular".
#Si el promedio es <4 mostrar "Reprobado".

#Se pide al usuario que ingrese las notas
nota1=int(input("Ingrese la primera nota:"))
nota2=int(input("Ingrese la segunda nota:"))
nota3=int(input("Ingrese la tercera nota:"))

#Se calcula el promedio de las notas
promedio=(nota1+nota2+nota3)/3

#Primera condición: si el promedio es 7 o más, está promocionado
if promedio>=7:
    print("Promocionado")
else:
    if promedio>=4:         #Segunda condición: si no llegó a 7 pero tiene 4 o más, es regular
        print("Regular")
    else:                   #Si no cumple ninguna de las anteriores, está reprobado
        print("Reprobado")