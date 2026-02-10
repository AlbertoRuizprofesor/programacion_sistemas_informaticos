#Realizar la carga de dos nombres por teclado. Mostrar cual de los dos es mayor alfabéticamente o si son iguales.

#Almacena los nombres en las variables nombre1 y nombre2
nombre1 = input("Introduzca el primer nombre: ")
nombre2 = input("Introduzca el segundo nombre: ")


#Determina qué nombre es mayor alfabéticamente y lo imprime en consola
if nombre1 == nombre2:
    print("Los dos nombres son iguales")
else:
    if nombre1 > nombre2:
        print(f"{nombre1} es mayor alfabéticamente")
    else:
        print(f"{nombre2} es mayor alfabéticamente")