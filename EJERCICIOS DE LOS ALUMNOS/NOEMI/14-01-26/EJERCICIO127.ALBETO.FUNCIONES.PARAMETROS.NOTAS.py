
#Ejercicio notas 127 ALBERTO con funciones y parametros:

def cargar_nota():
    notas=[]
    for i in range(5):
        nota=float(input(f"Introduce la nota {i+1}:"))
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas)/len(notas)

def mostrar_resultado(media):
    if media>=5:
        print("Has aprobado con una media de", media)
    else:
        print("Has suspendido con una media de ", media)
        
        
#LLamadas a funciones:   


media=calcular_media(cargar_nota())  #Se ejecuta desde dentro hacia fuera cargar_nota() se refiere a la lista
mostrar_resultado(media)
