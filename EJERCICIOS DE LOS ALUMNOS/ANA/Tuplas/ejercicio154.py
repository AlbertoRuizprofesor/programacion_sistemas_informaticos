# Se tiene que cargar los votos obtenidos por tres candidatos a una elección. 
# En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia 
# y la cantidad de votos obtenidos en dicha provincia.
# 1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
# 2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.

def cargar_candidatos():
    
    candidatos = [] 

    print("Introduzca los datos de los candidatos: ")

    for i in range(3): 

        nombre = input(f"Nombre candidato {i}: ")
        numprovincias = int(input("¿De cuantas provincias debemos guardar votos?: "))
        provincias = [] 
        for j in range(numprovincias): 
            provincia = input("Nombre de provincia: ")
            votos = int(input("Numero de votos: "))
            provincias.append((provincia,votos)) 
        candidatos.append((nombre, provincias)) 
    return candidatos 

def recuentovotos_candidatos(candidatos):
    
    for i in range(len(candidatos)):
        suma = 0 
        for j in range(len(candidatos[i][1])): 
        
        print(candidatos[i][0], suma) 
# Programa
candidatos = cargar_candidatos()
recuentovotos_candidatos(candidatos)
