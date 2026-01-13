"""
3º Vamos a añadir un descuento o rebaja del 30%, este descuento
se ha de realizar sobre el total, no sobre el total a pagar
"""

importe = int(input("Introduce el importe: "))
iva = importe * 0.21
total = importe + iva
descuento = total * 0.30

entregado = int(input("Dinero entregado: "))
cambio = entregado - (total - descuento)

print("El importe es:" , importe)
print("El iva es:" , iva)
print("El total es:" , total)
print("El descuento es:" , descuento)


print("El dinero entregado es:" , entregado)
print("El cambio es:" , cambio)



