"""
Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. (No se ingresan valores por teclado)

"""
contador = 0        #Contador para saber cuántas veces hemos repetido el bucle
numero = 0          #Número que iremos incrementando de 11 en 11

while contador < 25:               #Repetimos mientras contador sea menor de 25
    numero = numero + 11

    if contador < 24:                   #Los 24 primeros llevan guion
        print(f"{numero} -", end=" ")   
    else:                               #El último sin guion ni espacio
        print(f"{numero}")
    contador += 1

