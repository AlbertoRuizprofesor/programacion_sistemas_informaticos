# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:

n = int(input("Cuantos triángulos procesará: "))
cantidad = 0

for x in range(n):
    x = x + 1
    # a) De cada triángulo la medida de su base, su altura y su superficie.
    print(f"\nTriángulo num {x}:")
    base=int(input("Base: "))
    altura=int(input("Altura: "))
    superficie = base * altura / 2
    print(f"La superficie es {superficie}")
    
    # b) La cantidad de triángulos cuya superficie es mayor a 12.
    if superficie > 12:
        cantidad = cantidad+1

print(f"\nLa cantidad de triángulos con superficie superior a 12 son {cantidad}")