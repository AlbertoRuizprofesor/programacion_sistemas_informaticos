

alturas = []          #Lista vacía donde guardaremos las alturas introducidas

suma = 0              #Acumulador para sumar todas las alturas

for x in range(5):    #Bucle que se repetirá 5 veces
    valor = float(input("Introduzca la altura: "))  #Pedimos una altura al usuario
    alturas.append(valor)                           #Guardamos la altura en la lista
    suma = suma + valor                             #Sumamos la altura al acumulador

print(f"Las alturas ingresadas son {alturas}")       #Mostramos la lista completa

promedio = suma / 5                                  #Calculamos el promedio
print(f"El promedio de las alturas es {promedio:.2f}")  #Mostramos el promedio con 2 decimales

altas = 0            #Contador de personas más altas que el promedio
bajas = 0            #Contador de personas más bajas que el promedio

for x in range(5):   #Recorremos nuevamente la lista
    if alturas[x] > promedio:        #Si la altura es mayor que el promedio...
       altas = altas + 1             #...sumamos al contador de "altas"
    else:
        if alturas[x] < promedio:    #Si es menor que el promedio...
            bajas = bajas + 1        #...sumamos al contador de "bajas"
        #Si es igual al promedio, no cuenta en ninguno de los dos

#Imprime en consola los resultados
print(f"La cantidad de personas más bajas al promedio es {bajas}")  
print(f"La cantidad de personas más altas al promedio es {altas}")




