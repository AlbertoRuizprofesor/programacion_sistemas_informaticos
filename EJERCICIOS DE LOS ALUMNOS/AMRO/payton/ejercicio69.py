##Definir una lista que almacene 5 enteros.
##Sumar todos sus elementos y mostrar dicha suma

lista=[9,2,6,16,77]
suma=0
x=0
while x<len(lista):
    suma=suma+lista[x]
    x=x+1
print("Los elemetos de la lista son")
print(lista)
print("La suma de todos sus elemntos es")
print(suma)    