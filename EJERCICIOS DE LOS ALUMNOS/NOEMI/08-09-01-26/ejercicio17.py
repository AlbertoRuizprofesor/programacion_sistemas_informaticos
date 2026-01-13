#Ejercicio 17:Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a) La cantidad de valores ingresados negativos.
#b) La cantidad de valores ingresados positivos.
#c) La cantidad de múltiplos de 15.
#d) El valor acumulado de los números ingresados que son pares.

cantNegativos=0
cantPositivos=0
cantidadMúltiplos=0
cantValorpares=0


for i in range(10):
    valores=int(input("Introduce díez valores: "))
    if valores<0:
        cantNegativos=cantNegativos+1
    
    else:
        if valores>0:
            cantPositivos=cantPositivos+1
            
    if valores%15==0:
        cantidadMúltiplos=cantidadMúltiplos+1
       
    if valores%2==0:
        cantValorpares=cantValorpares+valores      
        
        
print(f"Cantidad de números negativos: {cantNegativos}")
print(f"Cantidad de números positivos: {cantPositivos}")
print(f"Cantidad de números múltiplos de 15: ", cantidadMúltiplos)
print(f"Cantidad de números pares", cantValorpares)