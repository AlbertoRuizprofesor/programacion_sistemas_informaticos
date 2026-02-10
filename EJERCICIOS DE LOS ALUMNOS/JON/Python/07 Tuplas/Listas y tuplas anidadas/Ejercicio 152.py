print("Ejercicio 152")
print("")
print("")

def cargarpaispoblacion():
    paises=[]
    for x in range (5):
        pais=input("Introduce el nombre del país: ")
        pobl=int(input("Introduce el número de habitantes: "))
        paises.append((pais,pobl))
    return paises

def imprimir(paises):
    print("Países y su población: ")
    for i in range (len(paises)):
        print(paises[i][0],paises[i][1])
        
def paismaspoblado(paises):
    pos=0
    for i in range(1, len(paises)):
        if paises[i][1]>paises[pos][1]:
            pos=i
    print("El país con mayor número de habitantes: ",paises[pos][0])
            

paises=cargarpaispoblacion()
imprimir(paises)
paismaspoblado(paises)

print("Fin de programa")


