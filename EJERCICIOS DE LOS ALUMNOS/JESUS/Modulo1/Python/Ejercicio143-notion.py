#Confeccionar una función que reciba entre 2 y n (siendo n = 2,3,4,5,6 etc.) valores enteros, 
# retornar la suma de dichos parámetros.


def sumar(val1,val2,*lista):
    suma=val1+val2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma

#bloque del programa                         

print("la suma de valor1 y valor2") 
print(sumar(1,2))
print("la suma de valor1 valor2 valor3 valor4") #la funcion realiza la suma de todos los valores independientemente de cuantos sean 
print(sumar(1,2,3,4))
print("la suma de valores")
print(sumar(9,8,7,6,5,4,))