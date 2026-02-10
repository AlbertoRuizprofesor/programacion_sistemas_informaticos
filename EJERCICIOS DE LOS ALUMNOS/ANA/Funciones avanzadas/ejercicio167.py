

# 1) Carga de una lista de 5 nombres.
# 2) Ordenar alfabéticamente la lista.
# 3) Imprimir la lista de nombres

def cargar():
    
    nombres=[]
    
    for i in range(5):
        nombre=input("Ingrese nombre: ")
        nombres.append(nombre)
    
    return nombres


def ordenar(nombres):
    

    for i in range(4):
    
        for j in range(4):
    
            if nombres[j]>nombres[j+1]:
                aux=nombres[j]
                nombres[j]=nombres[j+1]
                nombres[j+1]=aux


def imprimir(nombres):

    for x in range(len(nombres)):
        print(nombres[x]," ",end="")


# Programa

nombres=cargar()
ordenar(nombres)
imprimir(nombres)
