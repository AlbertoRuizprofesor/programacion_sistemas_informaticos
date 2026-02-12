# productos={"manzanas":39, "peras":32, "lechuga":17}
# print(productos)


#En el bloque principal del programa definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. 
# Implementar una función para mostrar cada clave y valor.

def impr_paises(paises):
    for clave in paises:
        print(clave,paises[clave])



paises={"argentina":4000000, "españa":4600000, "brasil":1900000,"uruguay":3400000}
impr_paises(paises)