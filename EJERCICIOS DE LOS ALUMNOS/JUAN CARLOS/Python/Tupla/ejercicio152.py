"""
Lista 5 tuplas (país, habitantes). 3 funciones: cargar, imprimir, país más habitantes.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def cargar_paises():
    paises = []
    for cnt in range(5):
        nombre = input(f"País {cnt+1}: ").strip()
        habitantes = int(input("Habitantes (millones): "))
        paises.append((nombre, habitantes))
    return paises

def imprimir_paises(lista_paises):
    print("\nLISTADO PAISES:")
    for pais in lista_paises:
        print(f"{pais[0]}: {pais[1]:,} millones")

def pais_mayor_habitantes(lista_paises):
    pais_max = max(lista_paises, key=lambda x: x[1])
    print(f"País más habitado: {pais_max[0]} ({pais_max[1]:,} millones)")


#Main
lista_paises = cargar_paises()
mensaje("Carga completada")
imprimir_paises(lista_paises)
mensaje("Mayor población")
pais_mayor_habitantes(lista_paises)
mensaje("Fin del programa")
