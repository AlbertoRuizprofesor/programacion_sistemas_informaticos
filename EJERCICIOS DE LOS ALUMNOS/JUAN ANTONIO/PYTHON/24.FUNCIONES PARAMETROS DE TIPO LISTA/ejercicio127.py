#Definir por asignación una lista de enteros en el bloque principal del programa. 
# Elaborar tres funciones, la primera recibe la lista y retorna la suma de todos sus elementos, 
# la segunda recibe la lista y retorna el mayor valor y la última recibe la lista y retorna el menor.



#Función que suma todos los elementos de una lista
def sumarizar(lista):
    suma = 0                    #Inicializamos la variable suma en 0
    for x in range(len(lista)): #Recorremos los índices de la lista
        suma = suma + lista[x]  #Vamos acumulando cada elemento
    return suma                 #Devolvemos la suma total

#Función que obtiene el mayor valor de una lista
def mayor(lista):
    may = lista[0]                  #Suponemos que el primer elemento es el mayor
    for x in range(1, len(lista)):  #Recorremos desde el segundo elemento
        if lista[x] > may:          #Si encontramos uno mayor...
            may = lista[x]          #...lo actualizamos
    return may                      #Devolvemos el mayor encontrado


#Función que obtiene el menor valor de una lista
def menor(lista):
    men = lista[0]                  #Suponemos que le primer elemento es el menor
    for x in range(1,len(lista)):   #Recorremos desde el segundo elemento
        if lista[x] < men:          #Si encontramos uno menor...
            men = lista[x]          #...lo actualizamos
    return men                      #Devolvemos el menor encontrado

#Lista de valores
listavalores = [10, 56, 23, 120, 94]
print("La lista completa es: ")
print(listavalores)

#Llamamos a las funciones y mostramos los resultados
print("La suma de todos sus elementos es: ", sumarizar(listavalores))
print("El mayor valor de la lista es: ", mayor(listavalores))
print("El menor valor de la lista es: ", menor(listavalores))
