#Ejercicio 72: Definir por asignación una lista con 8 elementos enteros. Contar cuantos de dichos valores almacenan un valor superior a 100.

lista=[200,400,6,700,45,60,7000,28]
cantidad=0
x=0
while x<len(lista):
    if lista [x]>=100:
        cantidad=cantidad+1
        
    x=x+1
    
print("Valores de la lista: ",lista)
print("Valores mayores que 100: ", cantidad)