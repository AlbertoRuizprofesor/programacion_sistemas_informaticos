#Ejercicio listas y funciones de notas




def cargar_nota():                           #funcion con lista pero no como parametro
    notas = []                               #lista vacia 
    for i in range(5):                       #bucle que pide x veces la nota 
        nota = float(input(f"Introduce la nota {i+1}: "))
        notas.append(nota)
    return notas

def calcular_media(notas):                   #funcion que interactua con el valor de la funcion anterior porque tiene return
    return sum(notas) / len(notas)  

def mostrar_resultado(media):                #funcion que no devuelve ningun valor solo lo muestra por pantalla
    if media >= 5:
        print(f"Has aprobado con una media de {media:.2f}")
    else:
        print(f"Has suspendido con una media de {media:.2f}")
        
    #bloque del programa

media=calcular_media(cargar_nota())          #variable que "invoca" a las funciones 
mostrar_resultado(media)                     #funcion que interactua con la variable
