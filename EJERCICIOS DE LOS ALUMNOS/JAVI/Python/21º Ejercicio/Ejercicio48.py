"""
Desarrollar un programa que solicite la carga de 10 números e imprima
la suma de los últimos 5 valores ingresados.
"""

cantidad=0
for x in range(10):
    valor=int(input("Ingrese un valor:"))
    if x>4:
        cantidad=cantidad+valor
print("La suma de los últimos 5 valores es")
print(cantidad)

