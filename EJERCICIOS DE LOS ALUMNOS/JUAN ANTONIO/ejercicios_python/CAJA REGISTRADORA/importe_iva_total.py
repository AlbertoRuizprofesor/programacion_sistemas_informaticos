
#Programa para calcular el IVA del 21%
#Suma el IVA y calcula el precio total

#Pide el importe sin el IVA
importe = float(input("Introduce el importe sin IVA: "))

#Calcula el IVA
iva = importe * 0.21

#Calcula el precio total
total = importe + iva


#Impresión en pantalla de todos los datos
print("Importe: ", importe,"€")
print("IVA (21%): ", iva,"€")
print("Total: ", total,"€")