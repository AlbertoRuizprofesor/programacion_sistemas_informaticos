lista=[8,9,10,11,12,13,14,15]
contador=0
x=0

while x<len(lista):
    if lista[x]>10:
        contador +=1
    x=x+1

print("elementos: ",lista)
print("mayor que 10: ",contador)