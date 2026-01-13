#Ejercicio 8: Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.


n=int(input("Introduce la cantidad de triangulos: "))
cantidad=0
for i in range(n):
    base=float(input("Introduce la base del triángulo: "))
    altura=float(input("Introduce la altura del triángulo: "))
    superficie=base*altura/2
    
    print("Base:", base)
    print("Altura:", altura)
    print("Superficie:", superficie)
    
    if superficie>12:
         cantidad=cantidad+1
    
    
print("La cantidad de triángulos con superficie a 12 son", cantidad)
    
