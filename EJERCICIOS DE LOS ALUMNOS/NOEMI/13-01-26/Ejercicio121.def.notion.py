#Ejercicio 121: Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.

def retornar_mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
        
    return mayor
    

v1=int(input("Introducir un valor: "))
v2=int(input("Introducir un valor: "))
print(retornar_mayor(v1,v2))
    