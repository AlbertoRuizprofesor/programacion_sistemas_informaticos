#Ejercicio tipo  127 lista con parametros.

def sumatorio(listavalores):
    suma=0
    for i in range(len(listavalores)):
        suma=suma+listavalores[i]
    return suma

def mayor(listavalores):
    may=listavalores[0]  #Todos los indices se van a comparar con el 0.
    for i in range(1,len(listavalores)): #Empieza el índice 1 y avanza hasta el final. 
        if listavalores[i]>may: #Awuí se comienzan a comparar cual es mayor.
            may=listavalores[i] 
    return may

def menor(listavalores):
    men=listavalores[0]
    for i in range(1,len(listavalores)):
        if listavalores[i]<men:
            men=listavalores[i]
    return men

listavalores=[10,23,24,34,56,67]
print("La lista completa es", listavalores)
print("La suma de todos sus elementos es", mayor(listavalores))
print("El mayor de la lista es",mayor(listavalores))    
print("El menor de la lista es", menor(listavalores))    
    