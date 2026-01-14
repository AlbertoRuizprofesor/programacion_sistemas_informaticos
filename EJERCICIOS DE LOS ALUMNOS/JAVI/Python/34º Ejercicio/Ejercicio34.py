"""
Definir por asignación una lista con 8 elementos enteros. 
Contar cuantos de dichos valores almacenan un valor superior a 100.
"""


lista = [2, 34, 5, 12, 10, 4, 23, 19]
cantidad = 0
x = 0

while x < len(lista):
    if lista [x] > 100:
        cantidad = cantidad + 1
    x = x + 1

print("Los números de la lista mayores que 100 son: ")
print(cantidad)




