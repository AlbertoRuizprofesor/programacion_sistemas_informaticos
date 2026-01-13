"""Ejercicio tipos de iva

Me tiene que pedir un producto y un importe
si el producto es: bebida, alimentación el iva es del 7%
si el producto es: electrodoméstico, informática el iva es del 21%
si el pruducto es: Curso de informática, Curso de cocina el iva es del 0%

Resultado

Su producto es de informática
su importe 100
el iva es 21%: 21
el total rd: 121"""

producto = input("Dime el producto (bebida, electrodoméstico, curso): ")
importe = int(input("Dime el importe: "))

print("Su producto es: " , producto)
print("Su importe es: " , importe)

if producto == "bebida":
    print("El IVA es del 7%")
    print("El total es de: " , importe * 1.07)

if producto == "alimentación":
    print("El IVA es del 7%")
    print("El total es de: " , importe * 1.07)

if producto == "electrodoméstico":
    print("El IVA es del 21%")
    print("El total es de: " , importe * 1.21)

if producto == "curso":
    print("El IVA es del 0%")
    print("El total es de: " , importe)

    

