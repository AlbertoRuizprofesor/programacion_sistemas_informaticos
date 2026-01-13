alturas=[]
suma=0
for x in range(5):
    valor=float(input("Ingrese la altura:"))
    alturas.append(valor)
    suma=suma+valor

print("Las alturas ingresadas son")
print(alturas)
promedio=suma/5
print("El promedio de las alturas es")
print(promedio)

altas=0
bajas=0
for x in range(5):
    if alturas[x]>promedio:
       altas=altas+1
    else:
        if alturas[x]<promedio:
            bajas=bajas+1

print("La cantidad de personas mas bajas al promedio es")
print(bajas)
print("La cantidad de personas mas altas al promedio es")
print(altas)
