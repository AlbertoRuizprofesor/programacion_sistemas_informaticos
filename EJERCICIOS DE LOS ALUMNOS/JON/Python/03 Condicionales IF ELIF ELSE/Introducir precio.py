print("Calcular precio")
print("")

unidades=int(input("Introduzca la cantidad de camisas: "))
importe=int(input("Introduzca el importe: "))
metodopago=input("Introduzca el método de pago (tarjeta/efectivo): ")

subtotal=unidades*importe
descuento=subtotal*0.3
total= subtotal-descuento

print("El importe con descuento es:", total)
print("El IVA es: ", total*0.21)

if metodopago=="tarjeta":
    print("El importe total es: ", total*1.21)
else:
    print("El importe total es: ", total*1.21)
    contado=int(input("Introduzca el importe de pago en efectivo:"))
    print("Su cambio es: ", contado-(total*1.21))

print("")

