"""
1º Ejercicio, tiene que pedirme el importe por consola
y me tiene que salir el importe, el iva 21% y el total
"""

importe = int(input("Introduce el importe: "))
iva = importe * 0.21
total = importe + iva

print("El importe es: " , importe)
print("El iva es: " , iva)
print("El total es: " , total)


