

# 1) Cargar el diccionario.
# 2) Listado completo del diccionario.
# 3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.

def cargar_datos():

    diccionario = {}
    continua="s" 
    
    while continua == "s":

        castellano=input("Ingrese palabra en castellano: ") 
        ingles=input("Ingrese palabra en ingles: ") 
        diccionario[ingles]=castellano 
        continua=input("Quiere cargar otra palabra [s/n]: ")

    return diccionario


def imprimir(diccionario):

    print("Listado completo del diccionario")
    
    for ingles in diccionario: 
        print(ingles,diccionario[ingles]) 

def consulta_palabra(diccionario):
    

    pal=input("Ingrese la palabra en ingles a consultar:")
    
    if pal in diccionario: 
        print("En castellano significa:",diccionario[pal])


# Programa

diccionario=cargar_datos()
imprimir(diccionario)
consulta_palabra(diccionario)