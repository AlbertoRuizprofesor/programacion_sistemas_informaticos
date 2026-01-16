"""
Lista 3 candidatos: [(nombre, [lista_tuplas_provincia_votos])]. 2 funciones: cargar, totales.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def cargar_candidatos():
    candidatos = []
    for cnt in range(3):
        nombre = input(f"Candidato {cnt+1}: ").strip()
        print("Provincias (ENTER vacío termina):")

        provincias = []
        while True:
            prov = input("Provincia: ").strip()
            if not prov:  # ENTER vacío
                break
            votos = int(input("Votos: "))
            provincias.append((prov, votos))

        candidatos.append((nombre, provincias))
    return candidatos

def totales_votos(candidatos):
    print("\nTOTALES:")
    for candidato in candidatos:
        nombre = candidato[0]
        lista_prov = candidato[1]
        total = 0
        for tupla in lista_prov:
            provincia = tupla[0]  # nombre provincia
            votos = tupla[1]      # cantidad votos
            total += votos

        print(f"{nombre}: {total:,} votos")


#Main
candidatos = cargar_candidatos()
mensaje("Elección cargada")
totales_votos(candidatos)
mensaje("Fin del programa")
