#Diccionario ejercicio 159 : En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. Implementar una función para mostrar cada clave y valor

def imprimir(paises):
    for clave in paises:
        print(clave,paises[clave])
        
paises={"argentina":23939933,"españa":3434434,"brasil":3434344}
imprimir(paises)




