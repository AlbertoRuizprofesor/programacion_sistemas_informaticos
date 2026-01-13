"""Realizar la carga de dos nombres por teclado. 
Mostrar cual de los dos es mayor alfabéticamente o si son iguales."""

nombre1 = input("Introduce el nombre 1: ")
nombre2 = input("Introduce el nombre 2: ")

if nombre1 == nombre2:
    print("Los nombre son iguales")

else:
    if nombre1 > nombre2:
        print ("El orden es: " , nombre1 + " , " + nombre2)
    else:
        print ("El orden es: " , nombre2 + " , " + nombre1)




