print("Ejercicio 158")
print("")
print("")


def cargararticulos():
    articulos=[]
    for i in range (5):
        nom=input(f"Introduce el nombre del artículo {i+1}: ")
        precio=int(input(f"Introduce el precio del artículo {i+1}: "))
        articulos.append((nom,precio))
    return articulos

def imprimir(listarticulos):
    for i in range (len(listarticulos)):
        print(listarticulos[i])
    

def preciolimitado(listarticulos):
    precio=listarticulos[(1)]
    pvprango=[]
    i=0
    for precio in listarticulos:
        if 10<=precio[1]<=15:
            print(f"El artículo {listarticulos[i]} está en el rango de precios.")
            pvprango.append(listarticulos[i])
        i+=1
    return pvprango

            
            
#Cuerpo de programa

lista=cargararticulos()
imprimir(lista)
preciolimitado(lista)

print("Fin de programa")
