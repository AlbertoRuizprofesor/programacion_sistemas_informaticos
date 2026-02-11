#Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos.

def retorna_promedio(var1,var2,var3):
    promedio=(var1+var2+var3)/3
    return promedio 

#Pilar principal 

var1=int(input("ingresa el primer valor"))
var2=int(input("ingresa el segundo valor"))
var3=int(input("ingresa el tercer valor:"))
print("valor del promedio de los tres numeros", retorna_promedio(var1,var2,var3))