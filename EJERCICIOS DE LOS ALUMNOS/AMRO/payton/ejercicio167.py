def cargar():
    nombres=[]
    for x in range(5):
        nom=input("Ingrese nombre:")
        nombres.append(nom)
    return nombres


def ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux=nombres[x]
                nombres[x]=nombres[x+1]
                nombres[x+1]=aux


def imprimir(nombres):
    for x in range(len(nombres)):
        print(nombres[x]," ",end="")


# bloque main

nombres=cargar()
ordenar(nombres)
imprimir(nombres)