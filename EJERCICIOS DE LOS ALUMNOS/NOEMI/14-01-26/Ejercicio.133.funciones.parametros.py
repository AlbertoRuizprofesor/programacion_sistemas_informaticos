#Ejercicio 133: Confeccionar una función que cargue por teclado una lista de 5 enteros y la retorne. Una segunda función debe recibir una lista y retornar el mayor y el menor valor de la lista. Desde el bloque principal del programa llamar a ambas funciones e imprimir el mayor y el menor de la lista.


def carga_valores():
    lista=[]
    for i in range(5):
        valores=int(input(f"Introduce un {i+1} valor: "))
        lista.append(valores)
    return lista

def mayor_menor_lista(lista):
    mayor=lista[0]
    menor=lista[0]
    for i in range(1,len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
        else:
            if  lista[i]<menor:
                    menor=lista[i]
                
    return [mayor,menor]

#Bloque principal:

lista=carga_valores()
mayor, menor=mayor_menor_lista(lista)
print("El mayor elemento de la lista: ",mayor)
print("El menor elemento de la lista: ", menor)
        
        
        
#Este ultimo el bloque principal tambien se puede hacer asi:
#//rango=retornar_mayormenor(lista)
#//print("Mayor elemento de la lista:",rango[0])
#//print("Menor elemento de la lista:",rango[1])