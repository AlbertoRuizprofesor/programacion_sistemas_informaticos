alturas=[]
suma=0
for x in range(5):
    valor=float(input("Ingrese la altura del operario:"))
    alturas.append(valor)
    suma=suma+valor

print("Lista de alturas")
print(alturas)
promedio=suma/5
print("Promedio de alturas")
print(promedio)

altas=0
bajas=0
for x in range(5):
    if alturas[x]<promedio:
        bajas +=1
    else:
        if alturas[x]>promedio:
            altas +=1
print("bajas: ", bajas)
print("altas: ", altas)