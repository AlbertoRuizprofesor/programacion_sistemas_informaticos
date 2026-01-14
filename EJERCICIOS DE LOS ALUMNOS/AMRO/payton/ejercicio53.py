negativos=0
positivos=0
mult15=0
sumapares=0
for f in range(10):
    valor=int(input("Ingrese valor: "))
    if valor<0:
        negativos=negativos+1
    else:
        if valor>0:
            positivos=positivos+1
    if valor%15==0:
        mult15=mult15+1
    if valor%2==0:
        sumapares=sumapares+1
print("Cantidad de números positivos: ")
print(positivos)                   
print("Cantidad de números negativos: ")
print(negativos)
print("Cantidad de múltiplos de 15: ")
print(mult15)
print("Cantidad de números pares: ")
print(sumapares)     