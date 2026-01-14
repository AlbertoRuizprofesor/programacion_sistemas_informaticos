n=int(input("Cuantos triángulos va a procesar:"))
cantidad=0
for f in range(n):
    base=int(input("Ingrese el valor de la base del triángulo:"))
    altura=int(input("Ingrese el valor de la altura del triángulo:"))
    superficie=base*altura/2
    print("La superficie es ")
    print(superficie)
    if superficie>12:
        cantidad=cantidad+1
print("La cantidad de triángulos con superficie superior a 12 son ")
print(cantidad)        
        
                   