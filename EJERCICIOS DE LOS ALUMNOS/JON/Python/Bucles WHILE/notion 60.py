print ("Ejercicio notion 60")
print("")
print("")

opcion="si"
acum=0

while opcion=="si":
    n=int(input("Introduzca su número: "))
    acum=acum+n
    opcion=input("Quieres introducir otro número? (si/no):")

print("La suma de los valores introducidos es: ", acum)
