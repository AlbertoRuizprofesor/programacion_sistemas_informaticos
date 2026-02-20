"""
Desarrollar un programa que permita la carga de 10 valores por teclado y 
nos muestre posteriormente la suma de los valores ingresados y su promedio.
"""

contador = 0    #Inicializamos el contador en 0 para llevar la cuenta de cuántos números se han ingresado
suma = 0        #Inicializamos la suma en 0; aquí iremos acumulando los valores ingresados

while contador < 10:    #El bucle se repetirá mientras contador sea menor que 10
    numero = int(input("Ingrese un valor: "))   #Pedimos un número al usuario y lo convertimos a entero
    suma += numero      #Sumamos el número ingresado al total acumulado
    contador += 1       #Aumentamos el contador en 1 para acercarnos al final del bucle

print("La suma es:", suma)  #Mostramos la suma total delos 10 números ingresados
print("El promedio es:", suma / contador)   #Calculamos y mostramos el promedio dividiendo la suma entre 10
