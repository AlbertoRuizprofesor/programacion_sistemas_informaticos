#Ejercicio: Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los últimos 5 valores ingresados.

suma=0

for i in range(10):
    valor=int(input("Introduce el valor: "))
    if i>4:
        suma=suma+valor
        
print("La suma de los últimos 5 valores es ", suma)
    