print("Problema 7")
print("")
print("")

cantidad=0
n=int(input("¿Cuántos números enteros deseas introducir?: "))
for x in range(n):
    numero=int(input("Introduce un número entero: "))
    if numero>=1000:
        cantidad=cantidad+1
print("Cantidad de números mayores o iguales a 1000: ", cantidad)