
def mayor(v1,v2):
    if v1>v2:
        mayor=v1
    else:
        mayor=v2
    return mayor

valor1=int(input("Ingrese el primer valor:"))
valor2=int(input("Ingrese el segundo valor:"))
print("el mayor valor es: ",mayor(valor1,valor2))
