# Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
v1 = int(input("Ingrese el primer valor: "))
v2 = int(input("Ingrese el segundo valor: "))

def retornar_mayor(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2


mayor = retornar_mayor(v1,v2)
print(f"El mayor es: {mayor}")
