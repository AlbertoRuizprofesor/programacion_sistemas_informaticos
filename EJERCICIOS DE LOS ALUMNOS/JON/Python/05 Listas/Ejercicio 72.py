print(" Problemas propuestos 1.- Listas")
print("")
print("")

lista=[150, 200, 250, 300, 350, 400, 450, 500]
masde100=0
x=0
while x < len(lista):
    if lista[x] > 100:
        masde100=masde100+1
    x=x+1

print("El número de elementos mayores que 100 en la lista es: ", masde100)

print("Fin de programa!!!")