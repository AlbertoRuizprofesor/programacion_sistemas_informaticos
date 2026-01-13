importe=int(input("Ingrese el importe: "))
unidades=int(input("Ingrese la cantidad de unidades: "))
tipo_de_pago=input("Ingrese el tipo de pago (tarjeta/efectivo): ")

totalUnidades=importe*unidades
descuento=totalUnidades*0.30
iva=descuento*0.21
total=descuento+iva

print("El importe es:", importe)
print("Las unidades son:", unidades)
print("El total sin IVA es:", totalUnidades)
print("El descuento es (30%):", descuento)
print("El IVA es:", iva)
print("El total con IVA es:", total)

if tipo_de_pago=="tarjeta":
   print("El tipo de pago es tarjeta",total)
else:
   entrega=int(input("Ingrese entrega en metálico: ")) 
   total_devolver=entrega-total
   print("El tipo de pago es efectivo",total_devolver)
   
