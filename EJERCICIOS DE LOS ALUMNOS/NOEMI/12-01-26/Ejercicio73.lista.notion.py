#Ejercicio 73: Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista=[3,5,6,9,10]
x=0


print("La lista es ", lista)

while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1


