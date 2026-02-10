# Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su área.
# b) La cantidad de triángulos cuya superficie es mayor a 12.

b = int(input("Ingresa la medida de la base del triángulo: "))
h = int(input("Ingresa la medida de la altura del triángulo: ")) 
contador = 0
area = (b * h) / 2
print(f"La base del triángulo es {b}, la altura  {h}, y el área {area}")
if area > 12:
    contador = contador+1
print(f"La cantidad de triángulos cuya superficie es mayor a 12 es: {contador}")