print("Ejercicio 130")
print("")
print("")

# Desarrollar una función que reciba una lista de string y nos retorne 
# el que tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres 
# debe retornar el que tiene un valor de componente más baja. 
# En el bloque principal iniciamos por asignación la lista de string:

# palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
# print("Palabra con mas caracteres:",mascaracteres(palabras))



def mascaracteres(lista):
    mayor=len(lista[0])
    palabra=lista[0]
    for n in range(len(lista)):
        if len(lista[n])>mayor:
            mayor=len(lista[n])
            palabra=lista[n]
        elif len(lista[n])==mayor:
            if lista[n]<palabra:
                palabra=lista[n]
    return palabra

palabras=["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print("Palabra con mas caracteres:",mascaracteres(palabras))

print("Fin del programa")