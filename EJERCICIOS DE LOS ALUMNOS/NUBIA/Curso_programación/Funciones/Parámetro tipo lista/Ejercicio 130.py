# Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres.
# Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja.
# En el bloque principal iniciamos por asignación la lista de string:

lista_palabras = ["Clarinete", "Saxofón", "Bajo", "Flauta"]

def mas_larga():
    for palabra in lista_palabras:
        if len(palabra) == max(len(palabra) for palabra in lista_palabras):
            return palabra


print("Lista de palabras: ")

for each in lista_palabras:
    print("-", each)
    
print(f"La palabra más larga de la lista es: {mas_larga()}")
