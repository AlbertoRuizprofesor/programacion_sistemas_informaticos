"""
Desarrollar un programa que permita cargar n números enteros y luego nos informe cuántos valores fueron pares y cuántos impares. 
Emplear el operador “%” en la condición de la estructura condicional 
(este operador retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1)
"""

cantidad = int(input("¿Cuantos números va a introducir: "))  #Pregunta cuantos números va a introducir, lo pasa a entero y lo almacena
contador = 0    #Contador para el bucle while
pares = 0       #Contador de números pares
impares = 0     #Contador de números impares

while  contador < cantidad:      #Repetimos tantas veces como indicó el usuario
    numero = int(input("Introduzca un número: "))   #Pedimos un número al usuario

    if numero % 2 == 0:     #Si el número es par....
        pares += 1          #...incrementa el contador de números pares
    else:                   #Si es impar....
        impares += 1        #...incrementa el contador de números impares
    contador += 1

#Imprime en consola el resultado
print(f"La cantidad de numeros pares fueron: {pares}")
print(f"La cantidad de números impares fueron: {impares}")