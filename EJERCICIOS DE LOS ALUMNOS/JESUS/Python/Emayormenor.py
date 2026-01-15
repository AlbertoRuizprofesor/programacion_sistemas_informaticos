#Confeccionar un módulo que implemente dos funciones, una que retorne el mayor de dos enteros y otra que retorne el menor de dos enteros.

#En el módulo principal importar solo la función que retorne el mayor, luego cargar dos enteros y mostrar el mayor de ellos

def mayor(x1,x2):
    if x1>x2:
        return x1
    else:
        return x2


def menor(x1,x2):
    if x1<x2:
        return x1
    else:
        return x2

