print("Ejercicio 149")
print("")
print("")

# Confeccionar un programa con las siguientes funciones:
# 1) Cargar una lista de 5 enteros.
# 2) Retornar el mayor y menor valor de la lista mediante una tupla. 
#       Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor.

def cargar():
        lista=[]
        for i in range (5):
            valor=int(input(f"Introduzca el valor {i+1}: "))
            lista.append(valor)
        return lista

def mayor(lista):
    mayor=lista[0]
    for i in range (len(lista)):
        if mayor<lista[i]:
            mayor=lista[i]
    return mayor

def menor(lista):
    menor=lista[0]
    for i in range (len(lista)):
        if menor>lista[i]:
             menor=lista[i]
    return menor

            



lista=cargar()
tupla=tuple(lista)
print(f"El número mayor de la lista es: {mayor(tupla)}")
print(f"El número menor de la lista es: {menor(tupla)}")



