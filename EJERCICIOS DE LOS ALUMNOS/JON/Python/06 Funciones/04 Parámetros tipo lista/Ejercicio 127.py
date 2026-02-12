print("Ejercicio 127")
print("")
print("")

# Definir por asignación una lista de enteros en el bloque principal del programa. 
# Elaborar tres funciones, la primera recibe la lista y retorna la suma 
# de todos sus elementos, la segunda recibe la lista y retorna el mayor valor 
# y la última recibe la lista y retorna el menor.

def sumar_lista(lista):
    suma=0
    for n in range(len(lista)):
        suma+=lista[n]
    return suma

def mayor_lista(lista):
    mayor=lista[0]
    for n in range(len(lista)):
        if lista[n]>mayor:
            mayor=lista[n]
    return mayor

def menor_lista(lista):
    menor=lista[0]
    for n in range(len(lista)):
        if lista[n]<menor:
            menor=lista[n]
    return menor

lista=[10, 56, 23, 120, 94]
print("La lista completa es:", lista)
print("La suma de todos los elementos es:", sumar_lista(lista))
print("El mayor valor de la lista es:", mayor_lista(lista)) 
print("El menor valor de la lista es:", menor_lista(lista))


print("Fin del programa")