cantidad = 0

n=int(input("Cuántos valores vas a dar: "))

for x in range (n):
    num = int (input("Introduce un número: "))

    if num >= 1000:
        cantidad = cantidad+1

    print("La cantidad de valores mayores o iguales a 1000 es: ")
    print(cantidad)
    


