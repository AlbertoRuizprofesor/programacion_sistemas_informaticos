"""
Cargar lista 5 enteros → función retorna tupla (mayor, menor) → desempaquetar main.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

def cargar_lista():
    lista = []
    for cnt in range(5):
        valor = int(input(f"Valor {cnt+1}: "))
        lista.append(valor)
    return lista

def mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    return (mayor, menor)  # Tupla


#Main
lista_numeros = cargar_lista()
mensaje("Lista cargada")

mayor, menor = mayor_menor(lista_numeros)  # ← Desempaquetar tupla
mensaje("Mayor y menor")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")

mensaje("Fin del programa")
