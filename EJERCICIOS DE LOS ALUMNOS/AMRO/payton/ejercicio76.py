lista=[]
valor=int(input("Ingrese un valor entero (0 para finalizar):"))
while valor!=0:
    valor=lista.append(valor)
    valor=int(input("Ingrese un valor entero (0 para finalizar):"))

print("El tamaño de la lista es:")
print(len(lista))    