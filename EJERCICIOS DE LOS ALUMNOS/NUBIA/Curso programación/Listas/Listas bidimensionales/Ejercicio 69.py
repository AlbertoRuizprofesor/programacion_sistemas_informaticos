# Definir una lista que almacene 5 enteros. Sumar todos sus elementos y mostrar dicha suma.

lista = [1,2,3,4,5]
suma = 0
x = 0
while x < len (lista):
    suma=suma+lista[x]
    x = x + 1
print("Los elementos de la lista son")
print(lista)
print("La suma de todos sus elementos es")
print(suma)
