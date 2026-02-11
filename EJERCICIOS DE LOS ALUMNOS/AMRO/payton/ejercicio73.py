lista=[1, 2, 56, 500, 698, 4, 6004, 41]
cantidad=0
x=0
while x<len(lista):
    if lista[x]>=7:
        cantidad=cantidad+1
    x=x+1

print("La lista está compuesta por los siguientes elementos:")
print(lista)
print("La cantidad de valores superiores o iguales a 7 en la lista son:")
print(cantidad)     
