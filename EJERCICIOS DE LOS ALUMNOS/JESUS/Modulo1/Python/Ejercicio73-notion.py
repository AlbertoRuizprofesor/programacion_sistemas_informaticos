#Definir una lista por asignación con 5 enteros. 
#Mostrar por pantalla solo los elementos con valor iguales o superiores a 7.

lista=[8,1,9,2,10]
x=0
print("Elementos de la lista con valor igual o superior a 7")
while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1