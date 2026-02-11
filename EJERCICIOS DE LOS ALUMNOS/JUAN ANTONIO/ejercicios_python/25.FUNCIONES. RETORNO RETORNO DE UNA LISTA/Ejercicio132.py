#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
# Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10.
#  Desde el bloque principal del programa llamar a ambas funciones.



#Función que carga una lista con 5 valores introducidos por el usuario
def carga_lista():
    li = []                    #Creamos una lista vacía donde guardamos los valores
    for x in range(5):         #Repetimos 5 veces (x toma valores 0, 1, 2, 3, 4,)
        valor = int(input("Ingrese valor: "))   #Pedimos un número al usuario
        li.append(valor)        #Añadimos el número a la lista
    return li                   #Devolvemos la lista completa


#Función que imprime solo los valores mayores a 10
def imprimir_mayor10(li):
    print("Elementos de la lista mayores a 10") 
    for x in range(len(li)):    #Recorremos la lista usando sus índices
        if li[x] > 10:          #Si el elemento actual es mayor que 10...
            print(li[x])        #...lo mostramos por pantalla

#------bloque principal del programa-----------

lista = carga_lista()       #Llamamos a la función para cargar la lista con valores
imprimir_mayor10(lista)     #Mostramos solo los valores mayores a 10