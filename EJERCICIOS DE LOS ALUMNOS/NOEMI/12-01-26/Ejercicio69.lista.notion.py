#Ejercicio 69: Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

Lista=[2,3,5,1,5]
suma=0
x=0

while x<len(Lista):
    suma=suma+Lista[x]
    x=x+1
print(f"Los elementos de la lista es {Lista}")
print(f"La suma de los elementos de la lista son: {suma}")

    