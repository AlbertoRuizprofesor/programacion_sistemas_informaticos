#Confeccionar una función que le enviemos como parámetros dos enteros y nos retorne el mayor.
def retorno_mayor(var1,var2):
    if var1>var2:
        mayor=var1
    else:
        mayor=var2
    return mayor

#pilar principal
var1=int(input("ingresa el primer valor:"))
var2=int(input("ingresa el segundo valor:"))
print(retorno_mayor(var1,var2))