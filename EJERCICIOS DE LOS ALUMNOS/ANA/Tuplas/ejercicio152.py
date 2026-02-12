# Almacenar en una lista de 5 elementos tuplas que guarden el nombre de un pais y la cantidad de habitantes.
# Definir tres funciones, en la primera cargar la lista, en la segunda imprimirla y en la tercera mostrar el nombre del país con mayor cantidad de habitantes.

def listatuplas_paises():
    
    paises = []
    print("Introduzca 5 datos de paises: ")

    for i in range(5):
        nombre = input(f"Nombre del pais {i}: ")
        habitantes = int(input(f"Numero de habitantes del pais {i}: "))
        paises.append((nombre,habitantes))
    
    return paises

def imprimir_paises(paises):

    print("Paises y población")

    for i in range(len(paises)):

        print(paises[i][0], paises[i][1]) 

    posmayor = 0 

    for i in range(len(paises)):
        if paises[i][1] > paises[posmayor][1]: 

    print("El país con mayor numero de habitantes es ", paises[posmayor][0])

# Programa
paises = listatuplas_paises()
imprimir_paises(paises)
paisconmashabitantes(paises)
