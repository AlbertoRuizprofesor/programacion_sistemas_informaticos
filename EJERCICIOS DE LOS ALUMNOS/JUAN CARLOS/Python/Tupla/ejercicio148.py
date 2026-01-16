"""
Definir tupla 3 enteros → lista → modificar → tupla.
"""

#Funciones
def mensaje(mensaje):
    print(f"=== === === {mensaje} === === ===")

#Main
tupla_original = (10, 20, 30)
mensaje("Tupla original")
print(f"{tupla_original}")

lista = list(tupla_original)  # Tupla → Lista
mensaje("Convertida a lista")
print(f"{lista}")

lista[1] = 50  # Modificar elemento central
mensaje("Lista modificada")
print(f"{lista}")

tupla_final = tuple(lista)  # Lista → Tupla
mensaje("Convertida a tupla")
print(f"{tupla_final}")

mensaje("Fin del programa")
