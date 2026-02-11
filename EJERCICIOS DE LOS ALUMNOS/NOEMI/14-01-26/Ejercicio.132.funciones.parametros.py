#Ejercicio 132: Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y mostrar todos los valores mayores a 10. Desde el bloque principal del programa llamar a ambas funciones.


def carga_lista():
    lista=[]
    for i in range(5):
        valor=int(input(f"Introduce el {i+1} valor: "))
        lista.append(valor)
    return lista

def mostrar_valoresmayor10(lista):
    print("Elementos de la lista mayores a 10.")
    for i in range(len(lista)):
        if lista[i]>10:
            print(lista[i])
            
            
lista=carga_lista()
mostrar_valoresmayor10(lista)
    