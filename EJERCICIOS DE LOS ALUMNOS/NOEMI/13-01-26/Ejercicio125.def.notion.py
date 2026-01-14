#Ejercicio 125: Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados: En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.


def retornar_superficie(lmenor,lmayor):     #La multiplicacion de los lados ocurre aqui y lo hace solo la funcion
    superficie=lmenor*lmayor
    return superficie

#BLOQUE PRINCIPAL

print("Primer rectángulo:")

l1=int(input("Introducir el valor del lado menor del rectángulo: "))
l2=int(input("Introducir el valor del lado del mayor rectángulo: "))  #Aquí se guardan las variables.

print("Segundo rectángulo:")

l3=int(input("Introducir el valor del lado menor del rectángulo: "))
l4=int(input("Introducir el valor del lado menor del rectángulo: "))


if retornar_superficie(l1,l2)==retornar_superficie(l3,l4):
    print("Los dos rectángulos tienen la misma superficie")
else:
    if retornar_superficie(l1,l2)>retornar_superficie(l3,l4):
        print("El primer rectángulo tiene la superficie mayor.")
    else:
        print("El segundo rectángulo tiene la superficie mayor.")

