#Ejercicios127Alberto_

def cargar_nota():
    notas = []
    for i in range(5):
        nota = float(input(f"Introduce la nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_media(notas):
    return sum(notas) / len(notas)  

def mostrar_resultado(media):
    if media >= 5:
        print(f"Has aprobado con una media de {media:.2f}")
    else:
        print(f"Has suspendido con una media de {media:.2f}")
        
media=calcular_media(cargar_nota())
mostrar_resultado(media)    
