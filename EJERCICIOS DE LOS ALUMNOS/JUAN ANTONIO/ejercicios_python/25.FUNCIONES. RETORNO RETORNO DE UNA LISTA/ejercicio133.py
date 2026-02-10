#Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. 
#Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. 
# Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.

#Función que carga una lista con 5 valores introducidos por el usuario
def carga_lista():
    li = []                     #Creamos una lista vacía
    for x in range(5):          #Repetimos 5 veces (x = 0, 1, 2, 3, 4)
        valor = int(input("Ingrese valor: "))   #Pedimos un número al usuario
        li.append(valor)        #Lo añadimos a la lista
    return li                   #Devolvemos la lista completa

#Función que devuelve el mayor y el menor valor de una lista
def retornar_mayormenor(li):
    ma = li[0]                  #Suponemos que el primer elemento es el mayor
    me = li[0]                  #Suponemos que el primer elemento es el menor
    
    #Recorremos la lista desde el segundo elemento
    for x in range(1, len(li)):
        if li[x] > ma:          #Si encontramos un valor mayor que el actual "ma", lo actualizamos
            ma = li[x]
        else:
            if li[x] < me:      #Si no es mayor, comprobamos si es menor que el acual "me"
                me = li[x]
    return [ma, me]            #Devolvemos ambos valores dentro de una lista

#--------bloque principal del programa-----------

lista = carga_lista()           #Cargamos la lista con valores del usuario
rango = retornar_mayormenor(lista)  #Obtenemos mayor y menor

print("Mayor elemento de la lista: ", rango[0]) #Mostramos el mayor
print("Menor elemento de la lista: ", rango[1]) #Mostramos el menor


