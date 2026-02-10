print("Ejercicio 161")
print("")
print("")

def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("introduzca palabra en castellano: ")
        ing=input("Introduzca palabra en inglés: ")
        diccionario[ing]=caste
        continua=input("Quieres añadir otra palabra? (s/n) ")
    return diccionario

def imprimir(diccionario):
    print("Listado completo de diccionario: ")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])
        
def buscarpalabra(diccionario):
    pal=input("Qué palabra en inglés quieres buscar???  ")
    if pal in diccionario:
        print(f"En castellano significa: {diccionario[pal]}")
        
diccionario=cargar()
imprimir(diccionario)
buscarpalabra(diccionario)

print("Fin del programa")

        