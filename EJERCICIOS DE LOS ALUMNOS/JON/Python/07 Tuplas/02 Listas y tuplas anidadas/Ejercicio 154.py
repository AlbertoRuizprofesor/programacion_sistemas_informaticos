print("Ejercicio 154")
print("")
print("")

def cargarvotos():
    votos=[]
    for i in range (3):
        candidato=input(f"Introduce el nombre del candidato {i+1}: ")
        nprov=input("Introduce el número de provincias: ")
        provincias=[]
        for x in range (nprov):
            prov=input(f"Introduce la provincia del candidato {i+1}: ")
            nvotos=int(input(f"Introduce el número de votos obtenidos por {candidato}"))
            provincias.append((prov,nvotos))

        
        votos.append([candidato,(prov,nvotos)])
    return votos

def mostrarvotos(votos):
    print("Los votos obtenidos por los candidatos son: ")
    for x in range (len(votos)):
        print(f"Candidato: {votos[x][0]} , Provincia: {votos[x][1][0] , Número de votos: {votos[x][1][1]} ")
              
    
votos=cargarvotos()
mostrarvotos(votos)


print("Fin del programa")
