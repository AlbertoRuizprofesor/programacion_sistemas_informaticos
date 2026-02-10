"""
- Se tiene que cargar los votos obtenidos por tres candidatos a una elección. En una lista cargar en la primer componente el nombre del candidato y en la segunda componente cargar una lista con componentes de tipo tupla con el nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas las provincias.
    
    Se deben cargar los datos por teclado, pero si se cargaran por asignación tendría una estructura similar a esta:
    

    candidatos=[ ("juan",[("cordoba",100),("buenos aires",200)]) , ("ana", [("cordoba",55)]) , ("luis", [("buenos aires",20)]) ]
"""

# -----------------------------------------
# Función: cargar_candidatos
# Pide los datos de 3 candidatos.
# Para cada candidato solicita:
#   - su nombre
#   - cuántas provincias quiere cargar
#   - por cada provincia: nombre y votos
# Guarda cada candidato como:
#   (nombre, [(provincia, votos), ...])
# Devuelve la lista completa.
# -----------------------------------------

def cargar_candidatos():
    lista_candidatos = []

    for i in range(3):
        nombre = input("Ingrese el nombre del candidato: ")
        cantidad_provincias = int(input("¿Cuántas provincias desea cargar? "))

        lista_provincias = []
        for j in range(cantidad_provincias):
            provincia = input("Nombre de la provincia: ")
            votos = int(input("Cantidad de votos: "))
            lista_provincias.append((provincia, votos))

        lista_candidatos.append((nombre, lista_provincias))

    return lista_candidatos


# -----------------------------------------
# Función: mostrar_total_votos
# Recorre la lista de candidatos y suma
# los votos de todas sus provincias.
# Imprime el total de cada candidato.
# -----------------------------------------

def mostrar_total_votos(candidatos):
    for i in range(len(candidatos)):
        total = 0

        # candidatos[i][1] es la lista de provincias
        for j in range(len(candidatos[i][1])):
            total += candidatos[i][1][j][1]   # Accede a los votos

        print(candidatos[i][0], total)         # candidatos[i][0] es el nombre


# -----------------------------------------
# Bloque principal del programa
# -----------------------------------------

candidatos = cargar_candidatos()
mostrar_total_votos(candidatos)

