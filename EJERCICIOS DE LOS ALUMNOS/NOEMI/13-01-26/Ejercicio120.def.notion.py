#Ejercicio 120: Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def retorno_funcion(valor): 
    sup=valor*valor
    return sup

valor=int(input("Introduce el valor del cuadrado: "))
superficie=retorno_funcion(valor)
print("La superficie del cuadrado es", superficie)


#Hecho por el profesor.

def retorno_funcion(lado): 
    sup=lado*lado
    return sup

valor=int(input("Introduce el valor del cuadrado: "))
superficie=retorno_funcion(valor)
print("La superficie del cuadrado es", superficie)