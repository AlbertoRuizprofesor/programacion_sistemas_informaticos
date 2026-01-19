"""
Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la medida de la base y la altura de un triángulo. El programa deberá informar:
a) De cada triángulo la medida de su base, su altura y su superficie.
b) La cantidad de triángulos cuya superficie es mayor a 12.

"""
#Pedimos cuántos triángulos se van a procesar
n=int(input("Cuantos triángulos procesará:"))

#Contador pra saber cuántos triángulos tienen superficie mayor a 12
cantidad=0

#Repetimos el proceso "n" veces
for x in range(n):
    basetri=int(input("Ingrese el valor de la base:")) #Pedimos la base del triángulo
    altura=int(input("Ingrese el valor de la altura:")) #Pedimos la altura del triángulo
    superficie=basetri*altura/2 #Calculamos la superficie usando la fórmula base * altura / 2
    print("La superficie es", superficie)   #Mostramos la superficie calculada
    #Si la superficie es mayor que 12, sumamos al contador
    if superficie>12:
        cantidad=cantidad+1

#Mostramos cuántos triángulos superan la superficie de 12
print("La cantidad de triángulos con superficie superior a 12 son", cantidad)
