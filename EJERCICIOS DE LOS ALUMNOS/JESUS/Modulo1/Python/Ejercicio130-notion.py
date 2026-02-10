# Desarrollar una función que reciba una lista de string y nos retorne el que tiene más caracteres. 
# Si hay más de uno con dicha cantidad de caracteres debe retornar el que tiene un valor de componente más baja. 
# En el bloque principal iniciamos por asignación la lista de string:

def mayorcaracteres(list_palabras): 
    posic=0
    for x in range(len(list_palabras)):
        if len(list_palabras[x])>len(list_palabras[posic]): #comparativa de la posicion en la lista y longitud con el siguiente elemento
            posic=x
    return list_palabras[posic]


#bloque del programa

list_palabras=["uno","dos","tres","cuatro","doscientos"]
print("palabra mas larga:", mayorcaracteres(list_palabras))