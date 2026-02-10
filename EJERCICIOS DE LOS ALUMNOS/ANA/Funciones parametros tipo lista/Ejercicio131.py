#Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
#Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja. 
#En el bloque principal iniciamos por asignación la lista de string:

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))

def mascaracteres(lista):
    if not lista:
        return None
palabra_mas_larga = lista[0]

for palabra in lista:
    if len(palabra) > len(palabra_mas_lagar):
        palabra_mas_larga = palabra

    return palabra_mas_larga

print("palabra con mas caracteres:", mascaracteres(palabras))
