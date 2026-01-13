cantidad=0

n=int(input("cuantos valores ingresaras"))
for x in range(n):
    valor=int(input("ingrese el valor"))
    if valor>=1000:
        cantidad=cantidad+1
print("la cantidad de valores con la condicion es: ", cantidad)