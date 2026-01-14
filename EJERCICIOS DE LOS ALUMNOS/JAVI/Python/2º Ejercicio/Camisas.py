"""
2º Ahora vamos a hacer el siguiente cambio, añadimos las unidades y descripción
ambos me lo pida por consola:
"""

cantidad = int(input("Introduce las unidades: "))
importe = int(input("Introduce el importe: "))

iva = importe * 0.21
total = importe + iva

print ("Camisas\n")
print ("unidades: " , cantidad)

print ("El importe es: " , importe)
print ("El iva es : " , iva)
print ("El total a pagar es : " , total)

