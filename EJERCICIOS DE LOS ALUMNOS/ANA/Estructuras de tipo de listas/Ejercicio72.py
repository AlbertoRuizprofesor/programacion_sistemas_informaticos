#Definir por asignación una lista con 8 elementos enteros. 
#Contar cuantos de dichos valores almacenan un valor superior a 100.

lista=[100, 2300, 500,14000, 10, 800, 910, 430]
cantidad=0 #variable que lleva el conteo mayores a 100
r=0
while r<len(lista):
    if lista[r]>100:
        cantidad=cantidad+1 
    r=r+1

print("la lista contiene estos valores" , lista)
print("la cantidad de valores mayores que 100 en la lista son" , cantidad)
