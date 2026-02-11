"""
Realizar un programa que permita cargar dos listas de 15 valores cada una. 
Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""
x = 1     #Contador para saber cuántos valores llevamos ingresados
sumaLista1 = 0    #Acumulador para la suma de la primera lista
sumaLista2 = 0    #Acumulador para la suma de la segunda lista

print("LISTA 1")        #Indicamos que empieza la carga de primera lista

while x <= 15:          #Repetimos 15 veces (valores del 1 al 15)
    valor = int(input("Ingrese valor:"))  #Pedimos un número al usuario
    sumaLista1 = sumaLista1+valor         #Lo sumamos al acumulador de lista 1
    x += 1                               #Incrementamos el contador

print("LISTA 2")        #Comienzo de la segunda lista
x = 1                   #Reinicio del contador

while x <= 15:          #Otra vez se piden 15 valores
    valor = int(input("Ingrese valor:"))    #Pedimos un número
    sumaLista2 = sumaLista2+valor           #Lo sumamos al acumulador de la lista 2
    x += 1                                  #Incrementamos el contador

if sumaLista1 > sumaLista2:                 #Si la suma de la lista 1 es mayor...
    print("La LISTA 1 es mayor.")           #Imprimimos lista 1 mayor
else:
    if sumaLista2 > sumaLista1:             #Si la suma de la lista 2 es mayor
        print("La LISTA 2 es mayor.")       #Imprimimos lista 2 mayor
    else:
        print("LAS LISTAS SON IGUALES.")    #Si ninguna es mayor son iguales