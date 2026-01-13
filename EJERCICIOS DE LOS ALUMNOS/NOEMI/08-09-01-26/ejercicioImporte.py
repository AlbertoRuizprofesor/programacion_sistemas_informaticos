
#Ejercicio: Caja registradora de venta.

descripcion=("Camisetas rosas con margaritas")


importe=float(input("Ingrese el importe? "))

unidades=int(input("Ingrese las unidades:"))

pago=input("Ingrese el tipo de pago (tarjeta/efectivo):")

total=importe*unidades
totalyrebaja=total*0.30
totalreal=total-totalyrebaja

iva=totalreal*0.21
totalpagar=totalreal + iva

print(descripcion)
print("Las unidades son", unidades)
print("El importe es", importe)
print("El total sin IVA es", total)
print("Con el descuento (30%) es:", totalreal)
print("El IVA es", iva)
print("El total con IVA a pagar es", totalpagar)

dineroentregado=float(input("Entrega:"))
dineroadevolver=dineroentregado - totalpagar

print("El total a devolver es", dineroadevolver)

if pago=="tarjeta":
    print("El tipo de pago es tarjeta", totalpagar)
else:
    entrega=int(input("Ingrese entrega en metálico: "))
    dineroadevolver=entrega-totalpagar
    print("el tipo de pago es efectivo",dineroadevolver)