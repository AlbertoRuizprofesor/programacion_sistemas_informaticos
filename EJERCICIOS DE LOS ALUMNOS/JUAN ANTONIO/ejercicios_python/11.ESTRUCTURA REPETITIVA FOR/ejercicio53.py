"""
Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
a) La cantidad de valores ingresados negativos.
b) La cantidad de valores ingresados positivos.
c) La cantidad de múltiplos de 15.
d) El valor acumulado de los números ingresados que son pares.

"""



#Contador de valores negativos
negativos = 0

#Contador de valores positivos
positivos = 0

#Contador de valores que son múltiplos de 15
multiplo15 = 0

#Acumulador para sumar todos los valores pares
sumapares = 0

#Se piden 10 valores al usuario
for f in range(10):
    valor = int(input("Ingrese valor:"))

    #Si el valor es negativo, aumentamos el contador de negativos
    if valor < 0:
        negativos = negativos+1
    else:   #Si no es negativo pero es mayor que 0, entonces es positivo
        if valor > 0:
            positivos = positivos+1
    if valor % 15 == 0:     #Si el valor es múltiplo de 15 (es decir, divisible por 15)
        multiplo15=multiplo15 + 1
    if valor % 2== 0:   #Si el valor es par, lo sumamos al acumulador
        sumapares = sumapares + valor

#Mostramos los resultados finales
print("Cantidad de valores negativos:", negativos)

print("Cantidad de valores positivos:", positivos)

print("Cantidad de valores múltiplos de 15:", multiplo15)

print("Suma de los valores pares:", sumapares)
