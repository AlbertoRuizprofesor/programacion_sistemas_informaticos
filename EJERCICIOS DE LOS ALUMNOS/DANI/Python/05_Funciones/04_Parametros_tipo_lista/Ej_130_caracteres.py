# Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
# Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja. 
def mascaracteres(lista):    
    pos=0
    for x in range(len(lista)):
        if len(lista[x])>len(lista[pos]):
            pos=x
    return lista[pos]

# En el bloque principal iniciamos por asignación la lista de string:
palabras=["enero", "febr", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))