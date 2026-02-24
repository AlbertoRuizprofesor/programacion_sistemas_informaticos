#Crear y cargar por teclado en el bloque principal del programa una lista de 5 enteros.
# Implementar una función que imprima el mayor y el menor valor de la lista.


#Función que recibe una lista y muestra el mayor y el menor valor
def mayor_menor(lista):
    #Suponemos que el primer valor de la lista es el mayor y el menor
    may = lista[0]
    men = lista[0]
    #Recorremos la lista desde el segundo elemento (indice 1)
    for x in range(1, len(lista)):
        if lista[x]  > may:     #Si el valor actual es mayor que el que teníamos guardado como mayor
            may = lista[x]      #Actualizamos el mayor
        else:                  
            if lista[x] < men:  #Si no es mayor, comprobamos si es menor que el que teníamos guardado como menor
                men = lista[x]  #Actualizamos el menor
    
    #Mostramos los resultados
    print("El valor mayor de la lista es ", may)
    print("El valor menor de la lista es", men)

#Creamos una lista vacía donde guardaremos los valores introducidos por el usuario
lista = []

#Pedimos 5 valores al usuario
for x in range(5):
    valor = int(input("Ingrese valor: "))
    lista.append(valor)     #Añadimos cada valor a la lista

#Llamamos a la función para calcular mayor y menor
mayor_menor(lista)