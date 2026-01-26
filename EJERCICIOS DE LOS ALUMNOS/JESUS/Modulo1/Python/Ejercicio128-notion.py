#Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. 
# Implementar una función que imprima el mayor y el menor valor de la lista.

def mayormenor(lista):    
    may=lista[0]
    men=lista[0]
    for x in range(1,len(lista)):
        if lista[x]>may:
            may=lista[x]
        else:
            if lista[x]<men:
                men=lista[x]
    print("Los valores mayor y menor de esta lista son ",may,men)

    #bloque del programa

lista=[]
for x in range(5):
    valor=int(input("Ingrese numero: "))
    lista.append(valor)
mayormenor(lista)