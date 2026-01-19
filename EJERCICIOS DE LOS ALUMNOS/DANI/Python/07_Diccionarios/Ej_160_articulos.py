# Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.

# Desarrollar además las funciones de:
# 1) Imprimir en forma completa el diccionario
def imprimir(diccionaro):
    for clave in diccionaro:
        print(clave, diccionaro[clave])
# 2) Imprimir solo los artículos con precio superior a 100.
def superior(diccionario):
    print("\nArticulos que valen más de 100€:")
    for clave in diccionario:
        if diccionario[clave] > 100:
            print(clave)




# ---------PROGRAMA PRINCIPAL---------
articulos = {
                "art1":100, 
                "art2":200,
                "art3":50,
                "art4":250,
                "art5":10
            }

imprimir(articulos)
superior(articulos)