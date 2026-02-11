lista=[101, 25, 56, 500, 698, 54, 6004, 41]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>100:
        cantidad=cantidad+1
    x=x+1

print("La lista está compuesta por los siguientes elementos:")
print(lista)
print("La cantidad de valores superiores a 100 en la lista son:")
print(cantidad)     
