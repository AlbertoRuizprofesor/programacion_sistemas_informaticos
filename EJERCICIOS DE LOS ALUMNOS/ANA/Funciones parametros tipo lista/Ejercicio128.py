#Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
#Implementar una función que imprima el mayor y el menor valor de la lista.

def mayormenor(lista):
    mayor=lista[0]
    menor=lista[0]
    
    for m in range(1, len(lista)):
        if lista [m]<menor:
            menor=lista[m]

    print("El valor mayor de la lista es", mayor)

#Pilar principal
lista=[]
for m in range (5):
    valor=int(input("ingrse el valor:"))
    lista.append(valor)
mayormenor(lista)
