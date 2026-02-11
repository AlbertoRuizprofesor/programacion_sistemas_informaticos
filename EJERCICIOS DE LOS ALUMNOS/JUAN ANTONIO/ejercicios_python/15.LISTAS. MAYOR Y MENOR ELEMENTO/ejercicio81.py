#Crear y cargar una lista con 5 enteros por teclado. 
#Implementar un algoritmo que identifique el menor valor de la lista y la posición donde se encuentra.

numeros = []                     #Creamos una lista vacía donde guardaremos los valores ingresados

for x in range(5):               #Repetimos 5 veces (índices del 0 al 4)
    valor = int(input("Ingrese un valor: "))  # Pedimos un número entero al usuario
    numeros.append(valor)        #Añadimos el número a la lista

menor = numeros[0]               #Suponemos que el primer elemento es el menor (punto de partida)
posicion = 0                     #Guardamos la posición inicial del menor (índice 0)

for x in range(1, 5):            #Recorremos la lista desde el segundo elemento hasta el último
    if numeros[x] < menor:       #Si encontramos un número más pequeño que el actual "menor"...
        menor = numeros[x]       #...actualizamos el valor del menor
        posicion = x             #...y guardamos la posición donde lo encontramos

print(f"La lista completa es: {numeros}")     #Mostramos la lista completa
print(f"El menor de la lista es: {menor}")    #Mostramos el valor más pequeño encontrado
print(f"La posición del menor es: {posicion}")#Mostramos la posición (índice) del menor
