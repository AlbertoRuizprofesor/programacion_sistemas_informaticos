#Escribir un programa que lea 10 números enteros y luego muestre cuántos valores ingresados fueron múltiplos de 3 y cuántos de 5. 
#Debemos tener en cuenta que hay números que son múltiplos de 3 y de 5 a la vez.

#Contadores para saber cuántos valores son múltiplos de 3 y de 5
multiplo3=0
multiplo5=0

#Repetimos el ingreso de valores 10 veces
for f in range(10):
    valor=int(input("Ingrese un valor:"))#Pedimos  un número al usuario y lo convertimos a entero
    if valor % 3 == 0:  #Si el valor es múltiplo de 3, aumentamos el contador correspondiente
        multiplo3= multiplo3 + 1
    if valor % 5 == 0:  #Si el valor es múltiplo de 5, aumentamos el otro contador
        multiplo5= multiplo5 + 1

#Mostramos cuántos valores fueron múltiplos de 3
print("Cantidad de valores ingresados múltiplos de 3:", multiplo3)

#Mostramos cuántos valores fueron múltiplos de 5
print("Cantidad de valores ingresados múltiplos de 5:", multiplo5)

