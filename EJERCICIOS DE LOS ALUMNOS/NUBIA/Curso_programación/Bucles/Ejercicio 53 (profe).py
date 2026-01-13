# Ejercicio 53.py

negativos=0
positivos=0
mult15=0
suma_pares=0
 
for f in range(10):
    valor=int(input("Ingrese valor entero:"))
    if valor<0:
        negativos=negativos+1
    else:
        if valor>0:
            positivos=positivos+1
    if valor%15==0:
        mult15=mult15+1
    if valor%2==0:
        suma_pares=suma_pares+valor

print("Cantidad de valores negativos:")
print(negativos)
print("Cantidad de valores positivos:")
print(positivos)
print("Cantidad de valores múltiplos de 15:")
print(mult15)
print("Suma de los valores pares:")
print(suma_pares)
