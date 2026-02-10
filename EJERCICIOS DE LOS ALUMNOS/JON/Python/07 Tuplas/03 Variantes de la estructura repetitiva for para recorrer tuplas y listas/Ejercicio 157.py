print("Ejercicio 157")
print("")
print("")

# Definir una función que cargue una lista con palabras y la retorne. 
# Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres

def cargar():
    lista=[]
    n=int(input("Cuántas palabras quieres añadir a la lista? "))
    for i in range (n):
        palabra=input(f"Introduzca la plalabra {i+1}: ")
        lista.append(palabra)
    return lista

def masde5(lista):
    masde5=[]
    palabra=lista
    c=0
    for palabra in lista:
        if len(palabra)>5:
            masde5.append(palabra)
            print(f"La palabra: {lista[c]} tiene más de 5 letras.")
        c+=1
    print(f"El número de palabras de más de 5 letras es: {len(masde5)}")
    return masde5

lista=cargar()
masde5(lista)
