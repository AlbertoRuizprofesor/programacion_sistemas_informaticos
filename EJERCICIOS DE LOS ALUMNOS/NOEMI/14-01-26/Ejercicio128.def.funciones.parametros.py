#Ejercicio 128: Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros. Implementar una función que imprima el mayor y el menor valor de la lista.


def mayor_menor(lista):
    mayor=lista[0]
    menor=lista[0]
    for i in range(5):
        if lista[i]>mayor:
            mayor=lista[i]
        else:
            if lista[i]<menor:
                menor=lista[i]
            
    print("El valor mayor de la lista es: ", mayor)
    print("El valor menor de la lista es ", menor)
    
    
    
lista=[]

for i in range(5):
    edad=int(input(f"Introduce su {i+1} edad:"))
    lista.append(edad)

mayor_menor(lista)    
    