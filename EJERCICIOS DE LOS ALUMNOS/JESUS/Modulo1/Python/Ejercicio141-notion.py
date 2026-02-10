# Cargar una lista de 10 enteros, 
# luego mostrarlos por pantalla a cada elemento separados por una coma.

def cargar_num():
    lista_num=[]
    for x in range(10):
        valor=int(input("Ingresa un numero: "))
        lista_num.append(valor)
    return lista_num

def imprim_lista(lista):
    for x in range(len(lista)):
        print(lista[x], end=",")


#bloque del programa 

lista=cargar_num()
imprim_lista(lista)