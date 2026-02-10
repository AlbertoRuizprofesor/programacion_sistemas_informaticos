print("Ejercicio 154")
print("")
print("")

def cargarvotos():
    votos=[]
    for i in range (3):
        nombre=input(f"Introduce el nombre del candidato {i+1}: ")
        nprov=int(input("Introduce el número de provincias: "))
        provincias=[]
        for x in range (nprov):
            prov=input(f"Introduce la provincia del candidato {i+1}: ")
            nvotos=int(input(f"Introduce el número de votos obtenidos por {nombre}: "))
            provincias.append((prov,nvotos))
        votos.append([nombre,provincias])
    return votos

def mostrarvotos(votos):
    print("Los votos obtenidos por los candidatos son: ")
    
    for x in range (len(votos)):
        nvotos=0
        for y in range (len(votos[x][1])):
            nvotos+=votos[x][1][y][1]
        print(f"El candidato {votos[x][0]} ha obtenido un total de {nvotos} votos.")

              
    
votos=cargarvotos()
mostrarvotos(votos)


print("Fin del programa")
